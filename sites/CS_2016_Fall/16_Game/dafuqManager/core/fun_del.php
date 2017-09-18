<?php
function del_items($dir) {
    if (($GLOBALS["permissions"] & 01) != 01) show_error($GLOBALS["error_msg"]["accessfunc"]);
    $cnt = count($GLOBALS['__POST']["selitems"]);
    $err = false;
    for ($i = 0;$i < $cnt;++$i) {
        $items[$i] = stripslashes($GLOBALS['__POST']["selitems"][$i]);
        $abs = get_abs_item($dir, $items[$i]);
        if (!@file_exists(get_abs_item($dir, $items[$i]))) {
            $error[$i] = $GLOBALS["error_msg"]["itemexist"];
            $err = true;
            continue;
        }
        if (!get_show_item($dir, $items[$i])) {
            $error[$i] = $GLOBALS["error_msg"]["accessitem"];
            $err = true;
            continue;
        }
        $ok = remove(get_abs_item($dir, $items[$i]));
        if ($ok === false) {
            $error[$i] = $GLOBALS["error_msg"]["delitem"];
            $err = true;
            continue;
        }
        $error[$i] = NULL;
    }
    if ($err) {
        $err_msg = "";
        for ($i = 0;$i < $cnt;++$i) {
            if ($error[$i] == NULL) continue;
            $err_msg.= $items[$i] . " : " . $error[$i] . "<BR>\n";
        }
        show_error($err_msg);
    }
    header("Location: " . make_link("list", $dir, NULL));
}
