<?php
// Conexion PDO a SQLite + creacion de la tabla si no existe.
// Requiere que config.php ya haya sido incluido (define RESERVAS_DB_PATH).

function reservas_db(): PDO
{
    static $pdo = null;
    if ($pdo !== null) {
        return $pdo;
    }

    $dbDir = dirname(RESERVAS_DB_PATH);
    if (!is_dir($dbDir)) {
        mkdir($dbDir, 0770, true);
    }

    $pdo = new PDO('sqlite:' . RESERVAS_DB_PATH);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->exec('PRAGMA foreign_keys = ON');

    $pdo->exec(<<<SQL
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            tour_slug TEXT NOT NULL,
            tour_title_es TEXT NOT NULL,
            tour_title_en TEXT NOT NULL,
            tour_date TEXT NOT NULL,
            tour_time TEXT NOT NULL DEFAULT '',
            meeting_point_es TEXT NOT NULL DEFAULT '',
            meeting_point_en TEXT NOT NULL DEFAULT '',
            client_name TEXT NOT NULL,
            client_phone TEXT NOT NULL DEFAULT '',
            hotel TEXT NOT NULL DEFAULT '',
            pickup_time TEXT NOT NULL DEFAULT '',
            num_people INTEGER NOT NULL DEFAULT 1,
            price_total TEXT NOT NULL DEFAULT '',
            currency TEXT NOT NULL DEFAULT 'PEN',
            payment_status TEXT NOT NULL DEFAULT 'pendiente',
            notes TEXT NOT NULL DEFAULT '',
            last_lang TEXT NOT NULL DEFAULT 'es'
        )
    SQL);

    $pdo->exec('CREATE INDEX IF NOT EXISTS idx_reservations_date ON reservations(tour_date)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS idx_reservations_slug ON reservations(tour_slug)');

    return $pdo;
}

// Genera el siguiente codigo de voucher del anio en curso: SM-2026-0001, SM-2026-0002, ...
function next_reservation_code(PDO $pdo): string
{
    $year = date('Y');
    $prefix = "SM-{$year}-";
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM reservations WHERE code LIKE ?");
    $stmt->execute([$prefix . '%']);
    $count = (int) $stmt->fetchColumn();

    for ($attempt = $count + 1; $attempt < $count + 1000; $attempt++) {
        $candidate = $prefix . str_pad((string) $attempt, 4, '0', STR_PAD_LEFT);
        $check = $pdo->prepare('SELECT 1 FROM reservations WHERE code = ?');
        $check->execute([$candidate]);
        if (!$check->fetchColumn()) {
            return $candidate;
        }
    }

    throw new RuntimeException('No se pudo generar un codigo de voucher unico.');
}
