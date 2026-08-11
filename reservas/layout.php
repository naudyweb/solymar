<?php
// Cabecera y pie de pagina comunes a todas las paginas de la herramienta de reservas.

function reservas_page_start(string $title, bool $showNav = true): void
{
    ?>
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title><?= htmlspecialchars($title, ENT_QUOTES) ?> · Reservas SolyMar Paracas</title>
    <link rel="icon" href="img/SolyMar-web.png" type="image/png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200;300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/reservas.css">
</head>
<body class="bg-surface font-manrope text-on-surface min-h-screen flex flex-col">
    <?php if ($showNav): ?>
    <header class="bg-primary text-white no-print">
        <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between gap-4 flex-wrap">
            <a href="index.php" class="flex items-center gap-2 font-bold text-lg">
                <img src="img/SolyMar-web.png" alt="SolyMar Paracas" class="h-8 w-auto bg-white rounded p-0.5">
                Reservas
            </a>
            <nav class="flex items-center gap-4 text-sm font-medium">
                <a href="index.php" class="hover:underline">Nueva reserva</a>
                <a href="historial.php" class="hover:underline">Historial</a>
                <a href="logout.php" class="hover:underline text-white/80">Salir</a>
            </nav>
        </div>
    </header>
    <?php endif; ?>
    <main class="flex-1">
    <?php
}

function reservas_page_end(): void
{
    ?>
    </main>
    <footer class="no-print text-center text-xs text-on-surface-variant py-6">
        SolyMar Paracas &middot; Herramienta interna de reservas
    </footer>
</body>
</html>
    <?php
}

// Muestra los mensajes flash guardados en sesion (uso: reservas_flash('ok', '...') antes de un redirect).
function reservas_set_flash(string $type, string $message): void
{
    $_SESSION['flash'] = ['type' => $type, 'message' => $message];
}

function reservas_render_flash(): void
{
    if (empty($_SESSION['flash'])) {
        return;
    }
    $flash = $_SESSION['flash'];
    unset($_SESSION['flash']);
    $color = $flash['type'] === 'error' ? 'bg-red-50 text-red-700 border-red-200' : 'bg-green-50 text-green-700 border-green-200';
    echo '<div class="max-w-5xl mx-auto px-4 pt-4"><div class="border rounded-lg px-4 py-3 text-sm ' . $color . '">'
        . htmlspecialchars($flash['message'], ENT_QUOTES) . '</div></div>';
}
