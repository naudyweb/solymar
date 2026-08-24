<?php
require_once __DIR__ . '/auth.php';
require_once __DIR__ . '/db.php';
require_once __DIR__ . '/tours.php';
require_once __DIR__ . '/strings.php';
require_once __DIR__ . '/layout.php';

$pdo = reservas_db();

$q = trim((string) ($_GET['q'] ?? ''));
$tourFilter = trim((string) ($_GET['tour'] ?? ''));
$from = trim((string) ($_GET['from'] ?? ''));
$to = trim((string) ($_GET['to'] ?? ''));

$where = [];
$params = [];

if ($q !== '') {
    $where[] = '(client_name LIKE :q OR code LIKE :q OR client_phone LIKE :q)';
    $params['q'] = '%' . $q . '%';
}
if ($tourFilter !== '') {
    $where[] = 'tour_slug = :tour';
    $params['tour'] = $tourFilter;
}
if ($from !== '') {
    $where[] = 'tour_date >= :from';
    $params['from'] = $from;
}
if ($to !== '') {
    $where[] = 'tour_date <= :to';
    $params['to'] = $to;
}

$sql = 'SELECT * FROM reservations';
if ($where) {
    $sql .= ' WHERE ' . implode(' AND ', $where);
}
$sql .= ' ORDER BY tour_date DESC, created_at DESC LIMIT 300';

$stmt = $pdo->prepare($sql);
$stmt->execute($params);
$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

reservas_page_start('Historial de reservas');
reservas_render_flash();
?>
<div class="max-w-6xl mx-auto px-4 py-8">
    <div class="flex items-center justify-between flex-wrap gap-3 mb-6">
        <h1 class="text-2xl font-bold text-primary">Historial de reservas</h1>
        <a href="index.php" class="bg-primary text-white font-semibold rounded-lg px-4 py-2 text-sm hover:bg-primary-container transition">+ Nueva reserva</a>
    </div>

    <form method="get" class="bg-white border border-surface-container rounded-2xl p-4 mb-6 grid sm:grid-cols-5 gap-3 items-end">
        <div class="sm:col-span-2">
            <label class="block text-xs font-medium mb-1 text-on-surface-variant">Buscar (nombre, codigo, telefono)</label>
            <input type="text" name="q" value="<?= htmlspecialchars($q, ENT_QUOTES) ?>"
                   class="w-full border border-surface-container rounded-lg px-3 py-2 text-sm">
        </div>
        <div>
            <label class="block text-xs font-medium mb-1 text-on-surface-variant">Tour</label>
            <select name="tour" class="w-full border border-surface-container rounded-lg px-3 py-2 text-sm">
                <option value="">Todos</option>
                <option value="<?= htmlspecialchars(RESERVAS_TRASLADO_VIP_SLUG, ENT_QUOTES) ?>" <?= $tourFilter === RESERVAS_TRASLADO_VIP_SLUG ? 'selected' : '' ?>>Traslado VIP</option>
                <?php foreach (reservas_tours() as $tour): ?>
                    <option value="<?= htmlspecialchars($tour['slug'], ENT_QUOTES) ?>" <?= $tourFilter === $tour['slug'] ? 'selected' : '' ?>>
                        <?= htmlspecialchars($tour['title_es'], ENT_QUOTES) ?>
                    </option>
                <?php endforeach; ?>
            </select>
        </div>
        <div>
            <label class="block text-xs font-medium mb-1 text-on-surface-variant">Desde</label>
            <input type="date" name="from" value="<?= htmlspecialchars($from, ENT_QUOTES) ?>"
                   class="w-full border border-surface-container rounded-lg px-3 py-2 text-sm">
        </div>
        <div>
            <label class="block text-xs font-medium mb-1 text-on-surface-variant">Hasta</label>
            <input type="date" name="to" value="<?= htmlspecialchars($to, ENT_QUOTES) ?>"
                   class="w-full border border-surface-container rounded-lg px-3 py-2 text-sm">
        </div>
        <div class="sm:col-span-5 flex gap-2">
            <button type="submit" class="bg-secondary text-white text-sm font-semibold rounded-lg px-4 py-2">Filtrar</button>
            <a href="historial.php" class="text-sm text-on-surface-variant self-center hover:underline">Limpiar filtros</a>
        </div>
    </form>

    <?php if (!$rows): ?>
        <p class="text-on-surface-variant text-sm">No hay reservas que coincidan con la busqueda.</p>
    <?php else: ?>
    <div class="bg-white border border-surface-container rounded-2xl overflow-x-auto">
        <table class="w-full text-sm min-w-[820px]">
            <thead class="bg-surface-container-low text-left text-on-surface-variant">
                <tr>
                    <th class="px-4 py-3">Codigo</th>
                    <th class="px-4 py-3">Cliente</th>
                    <th class="px-4 py-3">Tour</th>
                    <th class="px-4 py-3">Fecha</th>
                    <th class="px-4 py-3">Personas</th>
                    <th class="px-4 py-3">Precio</th>
                    <th class="px-4 py-3">Pago</th>
                    <th class="px-4 py-3"></th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($rows as $r): ?>
                <tr class="border-t border-surface-container">
                    <td class="px-4 py-3 font-mono"><?= htmlspecialchars($r['code'], ENT_QUOTES) ?></td>
                    <td class="px-4 py-3">
                        <?= htmlspecialchars($r['client_name'], ENT_QUOTES) ?>
                        <?php if ($r['client_phone']): ?><div class="text-xs text-on-surface-variant"><?= htmlspecialchars($r['client_phone'], ENT_QUOTES) ?></div><?php endif; ?>
                    </td>
                    <td class="px-4 py-3"><?= htmlspecialchars($r['tour_title_es'], ENT_QUOTES) ?></td>
                    <td class="px-4 py-3"><?= htmlspecialchars($r['tour_date'], ENT_QUOTES) ?></td>
                    <td class="px-4 py-3"><?= (int) $r['num_people'] ?></td>
                    <td class="px-4 py-3"><?= htmlspecialchars(reservas_format_price($r['price_total'], $r['currency']), ENT_QUOTES) ?></td>
                    <td class="px-4 py-3">
                        <span class="px-2 py-0.5 rounded-full text-xs font-medium
                            <?= $r['payment_status'] === 'pagado' ? 'bg-green-50 text-green-700' : ($r['payment_status'] === 'parcial' ? 'bg-amber-50 text-amber-700' : 'bg-red-50 text-red-700') ?>">
                            <?= htmlspecialchars(payment_status_label($r['payment_status'], 'es'), ENT_QUOTES) ?>
                        </span>
                    </td>
                    <td class="px-4 py-3 whitespace-nowrap text-right">
                        <a href="voucher.php?id=<?= (int) $r['id'] ?>" class="text-primary font-medium hover:underline">Ver</a>
                        <span class="text-on-surface-variant">·</span>
                        <a href="index.php?id=<?= (int) $r['id'] ?>" class="text-primary font-medium hover:underline">Editar</a>
                    </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
    <p class="text-xs text-on-surface-variant mt-3"><?= count($rows) ?> reserva(s) mostrada(s) (maximo 300).</p>
    <?php endif; ?>
</div>
<?php
reservas_page_end();
