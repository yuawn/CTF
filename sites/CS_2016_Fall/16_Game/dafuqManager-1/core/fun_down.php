<?php
require_once ('core/secure.php');
function download_item($dir, $item) {
    $item = basename($item);
    if (($GLOBALS["permissions"] & 01) != 01) show_error($GLOBALS["error_msg"]["accessfunc"]);
    if (!get_is_file($dir, $item)) show_error($item . ": " . $GLOBALS["error_msg"]["fileexist"]);
    if (!get_show_item($dir, $item)) show_error($item . ": " . $GLOBALS["error_msg"]["accessfile"]);
    $abs_item = get_abs_item($dir, $item);
    if (!file_in_web($abs_item) || stristr($abs_item, '.php') || stristr($abs_item, 'config')) show_error($item . ": " . $GLOBALS["error_msg"]["accessfile"]);
    $browser = id_browser();
    header('Content-Type: ' . (($browser == 'IE' || $browser == 'OPERA') ? 'application/octetstream' : 'application/octet-stream'));
    header('Expires: ' . gmdate('D, d M Y H:i:s') . ' GMT');
    header('Content-Transfer-Encoding: binary');
    header('Content-Length: ' . filesize($abs_item));
    if ($browser == 'IE') {
        header('Content-Disposition: attachment; filename="' . $item . '"');
        header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
        header('Pragma: public');
    } else {
        header('Content-Disposition: attachment; filename="' . $item . '"');
        header('Cache-Control: no-cache, must-revalidate');
        header('Pragma: no-cache');
    }
    @readfile($abs_item);
    exit;
}
