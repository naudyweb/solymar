<?php
// Textos bilingues usados en el voucher y en el resto de la herramienta.

const RESERVAS_STRINGS = [
    'voucher_title'    => ['es' => 'Voucher de Reserva', 'en' => 'Booking Voucher'],
    'code'             => ['es' => 'Codigo de reserva', 'en' => 'Booking code'],
    'client'           => ['es' => 'Cliente', 'en' => 'Client'],
    'phone'            => ['es' => 'Telefono / WhatsApp', 'en' => 'Phone / WhatsApp'],
    'tour'             => ['es' => 'Actividad', 'en' => 'Activity'],
    'date'             => ['es' => 'Fecha', 'en' => 'Date'],
    'time'             => ['es' => 'Hora', 'en' => 'Time'],
    'meeting_point'    => ['es' => 'Punto de encuentro / Horario', 'en' => 'Meeting point / Schedule'],
    'hotel'            => ['es' => 'Hotel', 'en' => 'Hotel'],
    'pickup_time'      => ['es' => 'Hora de recojo', 'en' => 'Pick-up time'],
    'num_people'       => ['es' => 'N° de personas', 'en' => 'Number of people'],
    'route'            => ['es' => 'Ruta', 'en' => 'Route'],
    'price_total'      => ['es' => 'Precio total', 'en' => 'Total price'],
    'payment_status'   => ['es' => 'Estado de pago', 'en' => 'Payment status'],
    'notes'            => ['es' => 'Notas', 'en' => 'Notes'],
    'issued_on'        => ['es' => 'Emitido el', 'en' => 'Issued on'],
    'footer_note'      => [
        'es' => 'Presenta este voucher (impreso o digital) el dia de tu actividad. Consultas: WhatsApp +51 961 542 547.',
        'en' => 'Show this voucher (printed or digital) on the day of your activity. Questions: WhatsApp +51 961 542 547.',
    ],
    'download_pdf'     => ['es' => 'Descargar PDF', 'en' => 'Download PDF'],
    'payment_pagado'   => ['es' => 'Pagado', 'en' => 'Paid'],
    'payment_pendiente'=> ['es' => 'Pendiente', 'en' => 'Pending'],
    'payment_parcial'  => ['es' => 'Pago parcial', 'en' => 'Partial payment'],
];

function t(string $key, string $lang): string
{
    $lang = $lang === 'en' ? 'en' : 'es';
    return RESERVAS_STRINGS[$key][$lang] ?? $key;
}

function payment_status_label(string $status, string $lang): string
{
    return t('payment_' . $status, $lang);
}

// Antepone el simbolo de moneda a un precio tipeado a mano si no lo trae ya
// (price_total es texto libre: los tours con calculo automatico ya incluyen
// el simbolo, pero uno escrito a mano -como en Traslado VIP- puede no traerlo).
// Se usa al guardar, para que el dato en la BD quede completo desde el origen.
function reservas_normalize_price(string $priceTotal, string $currency): string
{
    if ($priceTotal === '') {
        return '';
    }
    if (str_starts_with($priceTotal, 'S/') || str_starts_with($priceTotal, '$')) {
        return $priceTotal;
    }

    $symbol = $currency === 'USD' ? '$' : 'S/';
    return $symbol . ' ' . $priceTotal;
}

// Formatea el precio para mostrar (voucher/historial), cubriendo tambien
// reservas guardadas antes de que reservas_normalize_price existiera.
function reservas_format_price(string $priceTotal, string $currency): string
{
    $priceTotal = reservas_normalize_price(trim($priceTotal), $currency);
    if ($priceTotal === '') {
        $symbol = $currency === 'USD' ? '$' : 'S/';
        return $symbol . ' —';
    }

    return $priceTotal;
}

const RESERVAS_MONTHS = [
    'es' => ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
    'en' => ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
];

// Formatea una fecha Y-m-d (o una fecha/hora ISO) sin depender de la extension intl.
function format_date(string $dateStr, string $lang): string
{
    if ($dateStr === '') {
        return '';
    }
    $ts = strtotime($dateStr);
    if ($ts === false) {
        return $dateStr;
    }
    $day = (int) date('j', $ts);
    $month = RESERVAS_MONTHS[$lang === 'en' ? 'en' : 'es'][(int) date('n', $ts) - 1];
    $year = date('Y', $ts);

    return $lang === 'en' ? "{$month} {$day}, {$year}" : "{$day} de {$month} de {$year}";
}
