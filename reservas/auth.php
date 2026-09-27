<?php
// Incluir al inicio de toda pagina protegida: corta la ejecucion y redirige
// a login.php si no hay una sesion valida.
require_once __DIR__ . '/session.php';
require_once __DIR__ . '/config.php';

if (empty($_SESSION['reservas_auth'])) {
    header('Location: login.php');
    exit;
}

if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

function csrf_field(): string
{
    return '<input type="hidden" name="csrf_token" value="' . htmlspecialchars($_SESSION['csrf_token'], ENT_QUOTES) . '">';
}

function csrf_check(): void
{
    $token = $_POST['csrf_token'] ?? '';
    if (!hash_equals($_SESSION['csrf_token'] ?? '', $token)) {
        http_response_code(400);
        die('Token invalido. Vuelve a la pagina anterior e intentalo de nuevo.');
    }
}
