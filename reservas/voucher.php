<?php
require_once __DIR__ . '/auth.php';
require_once __DIR__ . '/db.php';
require_once __DIR__ . '/strings.php';
require_once __DIR__ . '/layout.php';

$pdo = reservas_db();
$id = (int) ($_GET['id'] ?? 0);
$lang = ($_GET['lang'] ?? '') === 'en' ? 'en' : (($_GET['lang'] ?? '') === 'es' ? 'es' : null);

$stmt = $pdo->prepare('SELECT * FROM reservations WHERE id = ?');
$stmt->execute([$id]);
$r = $stmt->fetch(PDO::FETCH_ASSOC);

if (!$r) {
    reservas_set_flash('error', 'No se encontro esa reserva.');
    header('Location: index.php');
    exit;
}

if ($lang === null) {
    $lang = $r['last_lang'] ?: 'es';
} elseif ($lang !== $r['last_lang']) {
    $pdo->prepare('UPDATE reservations SET last_lang = ? WHERE id = ?')->execute([$lang, $id]);
}

$tourTitle = $lang === 'en' ? $r['tour_title_en'] : $r['tour_title_es'];
$meetingPoint = $lang === 'en' ? $r['meeting_point_en'] : $r['meeting_point_es'];
$currencySymbol = $r['currency'] === 'USD' ? '$' : 'S/';

reservas_page_start('Voucher ' . $r['code']);
reservas_render_flash();
?>
<div class="max-w-2xl mx-auto px-4 py-8">
    <div class="no-print flex flex-wrap items-center justify-between gap-3 mb-4">
        <div class="flex gap-2 text-sm">
            <a href="voucher.php?id=<?= $id ?>&lang=es"
               class="px-3 py-1.5 rounded-full border <?= $lang === 'es' ? 'bg-primary text-white border-primary' : 'border-surface-container text-on-surface-variant' ?>">Espanol</a>
            <a href="voucher.php?id=<?= $id ?>&lang=en"
               class="px-3 py-1.5 rounded-full border <?= $lang === 'en' ? 'bg-primary text-white border-primary' : 'border-surface-container text-on-surface-variant' ?>">English</a>
        </div>
        <div class="flex gap-3 text-sm">
            <a href="index.php?id=<?= $id ?>" class="text-on-surface-variant hover:underline">Editar</a>
            <a href="historial.php" class="text-on-surface-variant hover:underline">Historial</a>
        </div>
    </div>

    <div id="voucher" class="bg-white border border-surface-container rounded-2xl shadow-sm p-8">
        <div class="flex items-center justify-between gap-4 border-b border-surface-container pb-6 mb-6">
            <img src="img/SolyMar-web.png" alt="SolyMar Paracas" class="h-12 w-auto">
            <div class="text-right">
                <div class="text-lg font-bold text-primary"><?= t('voucher_title', $lang) ?></div>
                <div class="text-sm text-on-surface-variant"><?= t('code', $lang) ?>: <span class="font-mono font-semibold"><?= htmlspecialchars($r['code'], ENT_QUOTES) ?></span></div>
            </div>
        </div>

        <h2 class="text-xl font-bold mb-4"><?= htmlspecialchars($tourTitle, ENT_QUOTES) ?></h2>

        <dl class="grid sm:grid-cols-2 gap-x-6 gap-y-4 text-sm">
            <div>
                <dt class="text-on-surface-variant"><?= t('client', $lang) ?></dt>
                <dd class="font-medium"><?= htmlspecialchars($r['client_name'], ENT_QUOTES) ?></dd>
            </div>
            <div>
                <dt class="text-on-surface-variant"><?= t('phone', $lang) ?></dt>
                <dd class="font-medium"><?= htmlspecialchars($r['client_phone'] ?: '—', ENT_QUOTES) ?></dd>
            </div>
            <div>
                <dt class="text-on-surface-variant"><?= t('date', $lang) ?></dt>
                <dd class="font-medium"><?= htmlspecialchars(format_date($r['tour_date'], $lang), ENT_QUOTES) ?></dd>
            </div>
            <div>
                <dt class="text-on-surface-variant"><?= t('time', $lang) ?></dt>
                <dd class="font-medium"><?= htmlspecialchars($r['tour_time'] ?: '—', ENT_QUOTES) ?></dd>
            </div>
            <div>
                <dt class="text-on-surface-variant"><?= t('hotel', $lang) ?></dt>
                <dd class="font-medium"><?= htmlspecialchars($r['hotel'] ?: '—', ENT_QUOTES) ?></dd>
            </div>
            <div>
                <dt class="text-on-surface-variant"><?= t('pickup_time', $lang) ?></dt>
                <dd class="font-medium"><?= htmlspecialchars($r['pickup_time'] ?: '—', ENT_QUOTES) ?></dd>
            </div>
            <div>
                <dt class="text-on-surface-variant"><?= t('num_people', $lang) ?></dt>
                <dd class="font-medium"><?= (int) $r['num_people'] ?></dd>
            </div>
            <div>
                <dt class="text-on-surface-variant"><?= t('price_total', $lang) ?></dt>
                <dd class="font-medium"><?= $r['price_total'] !== '' ? htmlspecialchars($r['price_total'], ENT_QUOTES) : htmlspecialchars($currencySymbol, ENT_QUOTES) . ' —' ?></dd>
            </div>
            <div>
                <dt class="text-on-surface-variant"><?= t('payment_status', $lang) ?></dt>
                <dd class="font-medium"><?= htmlspecialchars(payment_status_label($r['payment_status'], $lang), ENT_QUOTES) ?></dd>
            </div>
        </dl>

        <?php if ($meetingPoint !== ''): ?>
        <div class="mt-6 pt-6 border-t border-surface-container">
            <div class="text-on-surface-variant text-sm mb-1"><?= t('meeting_point', $lang) ?></div>
            <p class="text-sm whitespace-pre-line"><?= htmlspecialchars($meetingPoint, ENT_QUOTES) ?></p>
        </div>
        <?php endif; ?>

        <?php if ($r['notes'] !== ''): ?>
        <div class="mt-4">
            <div class="text-on-surface-variant text-sm mb-1"><?= t('notes', $lang) ?></div>
            <p class="text-sm whitespace-pre-line"><?= htmlspecialchars($r['notes'], ENT_QUOTES) ?></p>
        </div>
        <?php endif; ?>

        <div class="mt-8 pt-4 border-t border-surface-container text-xs text-on-surface-variant flex justify-between">
            <span><?= t('issued_on', $lang) ?>: <?= htmlspecialchars(format_date($r['created_at'], $lang), ENT_QUOTES) ?></span>
        </div>
        <p class="mt-4 text-xs text-on-surface-variant"><?= t('footer_note', $lang) ?></p>
    </div>

    <div class="no-print mt-6 text-center">
        <button id="download-pdf-btn" type="button"
                class="bg-tertiary text-on-tertiary font-semibold rounded-lg px-6 py-2.5 hover:opacity-90 transition inline-flex items-center gap-2">
            <?= t('download_pdf', $lang) ?>
        </button>
    </div>
</div>

<script src="js/html2pdf.bundle.min.js"></script>
<script>
document.getElementById('download-pdf-btn').addEventListener('click', function () {
    const el = document.getElementById('voucher');
    html2pdf().set({
        filename: 'Voucher-<?= htmlspecialchars($r['code'], ENT_QUOTES) ?>-<?= $lang ?>.pdf',
        margin: 10,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    }).from(el).save();
});
</script>
<?php
reservas_page_end();
