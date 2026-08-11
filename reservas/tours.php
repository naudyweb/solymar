<?php
// Catalogo de tours, leido desde tours.json (generado por ../export_tours_json.py
// a partir de generate_pages.py, la fuente de verdad del sitio publico).

function reservas_tours(): array
{
    static $tours = null;
    if ($tours !== null) {
        return $tours;
    }

    $path = __DIR__ . '/tours.json';
    if (!file_exists($path)) {
        throw new RuntimeException('reservas/tours.json no existe. Corre: python3 export_tours_json.py');
    }

    $tours = json_decode(file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
    return $tours;
}

function reservas_tour_by_slug(string $slug): ?array
{
    foreach (reservas_tours() as $tour) {
        if ($tour['slug'] === $slug) {
            return $tour;
        }
    }
    return null;
}

// Agrupa los tours por categoria, en el mismo orden que la pagina publica /tours.
function reservas_tours_by_category(): array
{
    $grouped = [];
    foreach (reservas_tours() as $tour) {
        $grouped[$tour['category']]['label_es'] = $tour['category_label_es'];
        $grouped[$tour['category']]['label_en'] = $tour['category_label_en'];
        $grouped[$tour['category']]['order'] = $tour['category_order'];
        $grouped[$tour['category']]['tours'][] = $tour;
    }
    uasort($grouped, fn($a, $b) => $a['order'] <=> $b['order']);
    return $grouped;
}
