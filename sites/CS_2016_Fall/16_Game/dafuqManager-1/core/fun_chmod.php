<?php
function chmod_item($dir, $item) {
    if (($GLOBALS["permissions"] & 01) != 01) show_error($GLOBALS["error_msg"]["accessfunc"]);
    if (!file_exists(get_abs_item($dir, $item))) show_error($item . ": " . $GLOBALS["error_msg"]["fileexist"]);
    if (!get_show_item($dir, $item)) show_error($item . ": " . $GLOBALS["error_msg"]["accessfile"]);
    if (isset($GLOBALS['__POST']["confirm"]) && $GLOBALS['__POST']["confirm"] == "true") {
        $bin = '';
        for ($i = 0;$i < 3;$i++) for ($j = 0;$j < 3;$j++) {
            $tmp = "r_" . $i . $j;
            if (isset($GLOBALS['__POST'][$tmp]) && $GLOBALS['__POST'][$tmp] == "1") $bin.= '1';
            else $bin.= '0';
        }
        if (!@chmod(get_abs_item($dir, $item), bindec($bin))) {
            show_error($item . ": " . $GLOBALS["error_msg"]["permchange"]);
        }
        header("Location: " . make_link("link", $dir, NULL));
        return;
    }
    $mode = parse_file_perms(get_file_perms($dir, $item));
    if ($mode === false) show_error($item . ": " . $GLOBALS["error_msg"]["permread"]);
    $pos = "rwx";
    $s_item = get_rel_item($dir, $item);
    if (strlen($s_item) > 50) $s_item = "..." . substr($s_item, -47);
    show_header($GLOBALS["messages"]["actperms"] . ": /" . $s_item);
    echo "<BR><TABLE width=\"175\"><FORM method=\"post\" action=\"";
    echo make_link("chmod", $dir, $item) . "\">\n";
    echo "<INPUT type=\"hidden\" name=\"confirm\" value=\"true\">\n";
    for ($i = 0;$i < 3;++$i) {
        echo "<TR><TD>" . $GLOBALS["messages"]["miscchmod"][$i] . "</TD>";
        for ($j = 0;$j < 3;++$j) {
            echo "<TD>" . $pos{$j} . "&nbsp;<INPUT type=\"checkbox\"";
            if ($mode{(3 * $i) + $j} != "-") echo " checked";
            echo " name=\"r_" . $i . $j . "\" value=\"1\"></TD>";
        }
        echo "</TR>\n";
    }
    echo "</TABLE>\n<BR><TABLE>\n<TR><TD>\n<INPUT type=\"submit\" value=\"" . $GLOBALS["messages"]["btnchange"];
    echo "\" class=\"button\"></TD>\n<TD><input type=\"button\" value=\"" . $GLOBALS["messages"]["btncancel"];
    echo "\" onClick=\"javascript:location='" . make_link("list", $dir, NULL) . "';\" class=\"button\">\n</TD></TR></FORM></TABLE><BR>\n";
}
