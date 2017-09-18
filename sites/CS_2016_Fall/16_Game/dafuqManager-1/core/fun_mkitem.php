<?php
function make_item($dir) {
    if (($GLOBALS["permissions"] & 01) != 01) show_error($GLOBALS["error_msg"]["accessfunc"]);
    $mkname = $GLOBALS['__POST']["mkname"];
    $mktype = $GLOBALS['__POST']["mktype"];
    $mkname = basename(stripslashes($mkname));
    if ($mkname == "") show_error($GLOBALS["error_msg"]["miscnoname"]);
    $new = get_abs_item($dir, $mkname);
    if (@file_exists($new)) show_error($mkname . ": " . $GLOBALS["error_msg"]["itemdoesexist"]);
    $bad = eregi($GLOBALS["allowed_file"], $new) == false;
    $ok = !$bad;
    if ($mktype != "file") {
        if (!$bad) $ok = @mkdir($new, 0777);
        $err = $GLOBALS["error_msg"]["createdir"];
    } else {
        if (!$bad) $ok = @touch($new);
        $err = $GLOBALS["error_msg"]["createfile"];
    }
    if ($ok === false) show_error($err);
    header("Location: " . make_link("list", $dir, NULL));
}
