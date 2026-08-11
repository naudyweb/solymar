<?php
require_once __DIR__ . '/auth.php';
require_once __DIR__ . '/db.php';
require_once __DIR__ . '/tours.php';
require_once __DIR__ . '/layout.php';

$pdo = reservas_db();
$editing = null;

if (isset($_GET['id'])) {
    $stmt = $pdo->prepare('SELECT * FROM reservations WHERE id = ?');
    $stmt->execute([(int) $_GET['id']]);
    $editing = $stmt->fetch(PDO::FETCH_ASSOC) ?: null;
    if (!$editing) {
        reservas_set_flash('error', 'No se encontro esa reserva.');
        header('Location: index.php');
        exit;
    }
}

$tours = reservas_tours();
$toursByCategory = reservas_tours_by_category();

reservas_page_start($editing ? 'Editar reserva' : 'Nueva reserva');
reservas_render_flash();
?>
<div class="max-w-3xl mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold text-primary mb-1"><?= $editing ? 'Editar reserva' : 'Nueva reserva' ?></h1>
    <p class="text-on-surface-variant text-sm mb-6">
        <?= $editing ? 'Codigo: ' . htmlspecialchars($editing['code'], ENT_QUOTES) : 'Completa los datos del cliente para generar el voucher.' ?>
    </p>

    <form method="post" action="guardar.php" id="reserva-form" class="space-y-6 bg-white border border-surface-container rounded-2xl p-6 shadow-sm">
        <?= csrf_field() ?>
        <?php if ($editing): ?>
            <input type="hidden" name="id" value="<?= (int) $editing['id'] ?>">
        <?php endif; ?>

        <div>
            <label for="tour_slug" class="block text-sm font-medium mb-1">Tour / Actividad *</label>
            <select id="tour_slug" name="tour_slug" required
                    class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
                <option value="">Selecciona un tour...</option>
                <?php foreach ($toursByCategory as $cat): ?>
                    <optgroup label="<?= htmlspecialchars($cat['label_es'], ENT_QUOTES) ?>">
                        <?php foreach ($cat['tours'] as $tour): ?>
                            <option value="<?= htmlspecialchars($tour['slug'], ENT_QUOTES) ?>"
                                <?= (isset($editing) && $editing['tour_slug'] === $tour['slug']) ? 'selected' : '' ?>>
                                <?= htmlspecialchars($tour['title_es'], ENT_QUOTES) ?>
                                (<?= htmlspecialchars($tour['price'], ENT_QUOTES) ?>)
                            </option>
                        <?php endforeach; ?>
                    </optgroup>
                <?php endforeach; ?>
            </select>
        </div>

        <div class="grid sm:grid-cols-2 gap-4">
            <div>
                <label for="tour_date" class="block text-sm font-medium mb-1">Fecha del tour *</label>
                <input type="date" id="tour_date" name="tour_date" required
                       value="<?= htmlspecialchars($editing['tour_date'] ?? '', ENT_QUOTES) ?>"
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
            <div>
                <label for="tour_time" class="block text-sm font-medium mb-1">Hora</label>
                <input type="text" id="tour_time" name="tour_time" placeholder="ej. 8:00 AM"
                       value="<?= htmlspecialchars($editing['tour_time'] ?? '', ENT_QUOTES) ?>"
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
        </div>

        <div class="grid sm:grid-cols-2 gap-4">
            <div>
                <label for="meeting_point_es" class="block text-sm font-medium mb-1">Punto de encuentro (Espanol)</label>
                <textarea id="meeting_point_es" name="meeting_point_es" rows="3"
                          class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary"><?= htmlspecialchars($editing['meeting_point_es'] ?? '', ENT_QUOTES) ?></textarea>
            </div>
            <div>
                <label for="meeting_point_en" class="block text-sm font-medium mb-1">Meeting point (English)</label>
                <textarea id="meeting_point_en" name="meeting_point_en" rows="3"
                          class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary"><?= htmlspecialchars($editing['meeting_point_en'] ?? '', ENT_QUOTES) ?></textarea>
            </div>
        </div>

        <div class="grid sm:grid-cols-2 gap-4">
            <div>
                <label for="client_name" class="block text-sm font-medium mb-1">Nombre del cliente *</label>
                <input type="text" id="client_name" name="client_name" required
                       value="<?= htmlspecialchars($editing['client_name'] ?? '', ENT_QUOTES) ?>"
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
            <div>
                <label for="client_phone" class="block text-sm font-medium mb-1">Telefono / WhatsApp</label>
                <input type="text" id="client_phone" name="client_phone"
                       value="<?= htmlspecialchars($editing['client_phone'] ?? '', ENT_QUOTES) ?>"
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
        </div>

        <div class="grid sm:grid-cols-2 gap-4">
            <div>
                <label for="hotel" class="block text-sm font-medium mb-1">Hotel</label>
                <input type="text" id="hotel" name="hotel"
                       value="<?= htmlspecialchars($editing['hotel'] ?? '', ENT_QUOTES) ?>"
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
            <div>
                <label for="pickup_time" class="block text-sm font-medium mb-1">Hora de recojo</label>
                <input type="text" id="pickup_time" name="pickup_time" placeholder="ej. 7:15 AM"
                       value="<?= htmlspecialchars($editing['pickup_time'] ?? '', ENT_QUOTES) ?>"
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
        </div>

        <div class="grid sm:grid-cols-3 gap-4">
            <div>
                <label for="num_people" class="block text-sm font-medium mb-1">N° de personas *</label>
                <input type="number" id="num_people" name="num_people" min="1" step="1" required
                       value="<?= htmlspecialchars((string) ($editing['num_people'] ?? 1), ENT_QUOTES) ?>"
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
            <div>
                <label for="price_total" class="block text-sm font-medium mb-1">Precio total</label>
                <input type="text" id="price_total" name="price_total"
                       value="<?= htmlspecialchars($editing['price_total'] ?? '', ENT_QUOTES) ?>"
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
            <div>
                <label for="currency" class="block text-sm font-medium mb-1">Moneda</label>
                <select id="currency" name="currency"
                        class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
                    <?php $cur = $editing['currency'] ?? 'PEN'; ?>
                    <option value="PEN" <?= $cur === 'PEN' ? 'selected' : '' ?>>S/ (PEN)</option>
                    <option value="USD" <?= $cur === 'USD' ? 'selected' : '' ?>>$ (USD)</option>
                </select>
            </div>
        </div>

        <div>
            <label for="payment_status" class="block text-sm font-medium mb-1">Estado de pago</label>
            <?php $status = $editing['payment_status'] ?? 'pendiente'; ?>
            <select id="payment_status" name="payment_status"
                    class="w-full sm:w-64 border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
                <option value="pendiente" <?= $status === 'pendiente' ? 'selected' : '' ?>>Pendiente</option>
                <option value="parcial" <?= $status === 'parcial' ? 'selected' : '' ?>>Pago parcial</option>
                <option value="pagado" <?= $status === 'pagado' ? 'selected' : '' ?>>Pagado</option>
            </select>
        </div>

        <div>
            <label for="notes" class="block text-sm font-medium mb-1">Notas internas</label>
            <textarea id="notes" name="notes" rows="3"
                      class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary"><?= htmlspecialchars($editing['notes'] ?? '', ENT_QUOTES) ?></textarea>
        </div>

        <div class="flex items-center gap-3 pt-2">
            <button type="submit"
                    class="bg-primary text-white font-semibold rounded-lg px-6 py-2 hover:bg-primary-container transition">
                <?= $editing ? 'Guardar cambios' : 'Generar voucher' ?>
            </button>
            <?php if ($editing): ?>
                <a href="voucher.php?id=<?= (int) $editing['id'] ?>" class="text-sm text-on-surface-variant hover:underline">Cancelar</a>
            <?php endif; ?>
        </div>
    </form>
</div>

<script>
const TOURS = <?= json_encode($tours, JSON_UNESCAPED_UNICODE) ?>;
const isEditing = <?= $editing ? 'true' : 'false' ?>;

document.getElementById('tour_slug').addEventListener('change', function () {
    if (isEditing) return; // no pisar datos ya guardados al editar
    const tour = TOURS.find(t => t.slug === this.value);
    if (!tour) return;

    document.getElementById('meeting_point_es').value = tour.schedule_es || '';
    document.getElementById('meeting_point_en').value = tour.schedule_en || '';
    document.getElementById('currency').value = tour.price_cur || 'PEN';

    if (tour.quote_only) {
        document.getElementById('price_total').value = '';
    } else {
        recalcPrice(tour);
    }
});

document.getElementById('num_people').addEventListener('input', function () {
    if (isEditing) return;
    const tour = TOURS.find(t => t.slug === document.getElementById('tour_slug').value);
    if (tour && !tour.quote_only) recalcPrice(tour);
});

function recalcPrice(tour) {
    const people = parseInt(document.getElementById('num_people').value || '1', 10);
    const total = parseFloat(tour.price_val) * (people || 1);
    const symbol = tour.price_cur === 'USD' ? '$' : 'S/';
    document.getElementById('price_total').value = `${symbol} ${total.toFixed(2)}`;
}
</script>
<?php
reservas_page_end();
