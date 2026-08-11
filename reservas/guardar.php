<?php
require_once __DIR__ . '/auth.php';
require_once __DIR__ . '/db.php';
require_once __DIR__ . '/tours.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: index.php');
    exit;
}

csrf_check();

$pdo = reservas_db();

$id = isset($_POST['id']) ? (int) $_POST['id'] : null;
$tourSlug = trim((string) ($_POST['tour_slug'] ?? ''));
$tour = reservas_tour_by_slug($tourSlug);
$clientName = trim((string) ($_POST['client_name'] ?? ''));
$tourDate = trim((string) ($_POST['tour_date'] ?? ''));
$numPeople = max(1, (int) ($_POST['num_people'] ?? 1));

if (!$tour || $clientName === '' || $tourDate === '') {
    reservas_set_flash('error', 'Completa el tour, la fecha y el nombre del cliente.');
    header('Location: index.php' . ($id ? '?id=' . $id : ''));
    exit;
}

$paymentStatus = in_array($_POST['payment_status'] ?? '', ['pendiente', 'parcial', 'pagado'], true)
    ? $_POST['payment_status']
    : 'pendiente';

$currency = in_array($_POST['currency'] ?? '', ['PEN', 'USD'], true) ? $_POST['currency'] : 'PEN';

$data = [
    'tour_slug' => $tour['slug'],
    'tour_title_es' => $tour['title_es'],
    'tour_title_en' => $tour['title_en'],
    'tour_date' => $tourDate,
    'tour_time' => trim((string) ($_POST['tour_time'] ?? '')),
    'meeting_point_es' => trim((string) ($_POST['meeting_point_es'] ?? '')),
    'meeting_point_en' => trim((string) ($_POST['meeting_point_en'] ?? '')),
    'client_name' => $clientName,
    'client_phone' => trim((string) ($_POST['client_phone'] ?? '')),
    'hotel' => trim((string) ($_POST['hotel'] ?? '')),
    'pickup_time' => trim((string) ($_POST['pickup_time'] ?? '')),
    'num_people' => $numPeople,
    'price_total' => trim((string) ($_POST['price_total'] ?? '')),
    'currency' => $currency,
    'payment_status' => $paymentStatus,
    'notes' => trim((string) ($_POST['notes'] ?? '')),
];

$now = date('c');

if ($id) {
    $check = $pdo->prepare('SELECT id, last_lang FROM reservations WHERE id = ?');
    $check->execute([$id]);
    $existing = $check->fetch(PDO::FETCH_ASSOC);
    if (!$existing) {
        reservas_set_flash('error', 'No se encontro esa reserva.');
        header('Location: index.php');
        exit;
    }

    $data['updated_at'] = $now;
    $sql = 'UPDATE reservations SET tour_slug=:tour_slug, tour_title_es=:tour_title_es, tour_title_en=:tour_title_en,
            tour_date=:tour_date, tour_time=:tour_time, meeting_point_es=:meeting_point_es, meeting_point_en=:meeting_point_en,
            client_name=:client_name, client_phone=:client_phone, hotel=:hotel, pickup_time=:pickup_time,
            num_people=:num_people, price_total=:price_total, currency=:currency, payment_status=:payment_status,
            notes=:notes, updated_at=:updated_at WHERE id=:id';
    $data['id'] = $id;
    $pdo->prepare($sql)->execute($data);

    header('Location: voucher.php?id=' . $id . '&lang=' . ($existing['last_lang'] ?: 'es'));
    exit;
}

$code = next_reservation_code($pdo);
$data['code'] = $code;
$data['created_at'] = $now;
$data['updated_at'] = $now;
$data['last_lang'] = 'es';

$sql = 'INSERT INTO reservations
        (code, created_at, updated_at, tour_slug, tour_title_es, tour_title_en, tour_date, tour_time,
         meeting_point_es, meeting_point_en, client_name, client_phone, hotel, pickup_time, num_people,
         price_total, currency, payment_status, notes, last_lang)
        VALUES
        (:code, :created_at, :updated_at, :tour_slug, :tour_title_es, :tour_title_en, :tour_date, :tour_time,
         :meeting_point_es, :meeting_point_en, :client_name, :client_phone, :hotel, :pickup_time, :num_people,
         :price_total, :currency, :payment_status, :notes, :last_lang)';
$pdo->prepare($sql)->execute($data);

header('Location: voucher.php?id=' . $pdo->lastInsertId() . '&lang=es');
exit;
