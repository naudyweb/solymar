<?php
require_once __DIR__ . '/session.php';
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/layout.php';

if (!empty($_SESSION['reservas_auth'])) {
    header('Location: index.php');
    exit;
}

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $password = (string) ($_POST['password'] ?? '');
    if ($password !== '' && password_verify($password, RESERVAS_PASSWORD_HASH)) {
        session_regenerate_id(true);
        $_SESSION['reservas_auth'] = true;
        header('Location: index.php');
        exit;
    }
    $error = 'Clave incorrecta. Intenta de nuevo.';
}

reservas_page_start('Iniciar sesion', false);
?>
<div class="max-w-sm mx-auto px-4 py-16">
    <div class="bg-white border border-surface-container rounded-2xl shadow-sm p-8">
        <img src="img/SolyMar-web.png" alt="SolyMar Paracas" class="h-10 w-auto mx-auto mb-6">
        <h1 class="text-lg font-bold text-center mb-1">Reservas · Personal interno</h1>
        <p class="text-sm text-on-surface-variant text-center mb-6">Ingresa la clave de acceso del equipo.</p>

        <?php if ($error !== ''): ?>
            <div class="bg-red-50 text-red-700 border border-red-200 rounded-lg px-4 py-2 text-sm mb-4">
                <?= htmlspecialchars($error, ENT_QUOTES) ?>
            </div>
        <?php endif; ?>

        <form method="post" class="space-y-4">
            <div>
                <label for="password" class="block text-sm font-medium mb-1">Clave</label>
                <input type="password" id="password" name="password" required autofocus
                       class="w-full border border-surface-container rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary">
            </div>
            <button type="submit"
                    class="w-full bg-primary text-white font-semibold rounded-lg py-2 hover:bg-primary-container transition">
                Entrar
            </button>
        </form>
    </div>
</div>
<?php
reservas_page_end();
