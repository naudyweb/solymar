<?php
// Extrae coordenadas (lat, lng) de lo que el personal pegue en el campo de
// ubicacion de recojo: coordenadas sueltas, un link normal de Google Maps
// (con @lat,lng o ?q=lat,lng), o un link corto (maps.app.goo.gl / goo.gl/maps)
// que primero hay que resolver siguiendo el redirect.

function extract_maps_coordinates(string $input): ?array
{
    $input = trim($input);
    if ($input === '') {
        return null;
    }

    $coords = find_coordinates_in_string($input);
    if ($coords) {
        return $coords;
    }

    if (looks_like_shortened_maps_link($input) && function_exists('curl_init')) {
        $resolved = resolve_redirect($input);
        if ($resolved) {
            return find_coordinates_in_string($resolved);
        }
    }

    return null;
}

function find_coordinates_in_string(string $text): ?array
{
    // Coordenadas sueltas: "-13.8355, -76.2531"
    if (preg_match('/^(-?\d{1,3}\.\d+),\s*(-?\d{1,3}\.\d+)$/', $text, $m)) {
        return [$m[1], $m[2]];
    }
    // Formato con @lat,lng,zoom (URL copiada desde la barra de direcciones)
    if (preg_match('/@(-?\d{1,3}\.\d+),(-?\d{1,3}\.\d+)/', $text, $m)) {
        return [$m[1], $m[2]];
    }
    // Parametros ?q=lat,lng o &ll=lat,lng
    if (preg_match('/[?&](?:q|ll)=(-?\d{1,3}\.\d+),(-?\d{1,3}\.\d+)/', $text, $m)) {
        return [$m[1], $m[2]];
    }
    return null;
}

function looks_like_shortened_maps_link(string $url): bool
{
    $host = parse_url($url, PHP_URL_HOST);
    return $host !== null && in_array(strtolower($host), ['maps.app.goo.gl', 'goo.gl'], true);
}

// Sigue redirects (HEAD) y devuelve la URL final, o null si falla.
function resolve_redirect(string $url): ?string
{
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_NOBODY => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_MAXREDIRS => 5,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 8,
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_USERAGENT => 'Mozilla/5.0 (compatible; SolyMarReservas/1.0)',
    ]);
    curl_exec($ch);
    $finalUrl = curl_getinfo($ch, CURLINFO_EFFECTIVE_URL);
    $error = curl_errno($ch);
    curl_close($ch);

    return ($error === 0 && $finalUrl) ? $finalUrl : null;
}

function google_maps_view_url(string $rawInput, string $lat, string $lng): string
{
    if ($lat !== '' && $lng !== '') {
        return "https://www.google.com/maps?q={$lat},{$lng}";
    }
    return $rawInput;
}

function google_static_map_url(string $lat, string $lng, int $width = 600, int $height = 280): ?string
{
    if (!defined('GOOGLE_MAPS_STATIC_API_KEY') || GOOGLE_MAPS_STATIC_API_KEY === '') {
        return null;
    }
    $params = http_build_query([
        'center' => "{$lat},{$lng}",
        'zoom' => 16,
        'size' => "{$width}x{$height}",
        'scale' => 2,
        'markers' => "color:red|{$lat},{$lng}",
        'key' => GOOGLE_MAPS_STATIC_API_KEY,
    ]);
    return "https://maps.googleapis.com/maps/api/staticmap?{$params}";
}
