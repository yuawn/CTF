<?php
function dir_list($dir) {
    $handle = @opendir(get_abs_dir($dir));
    if ($handle === false) return;
    while (($new_item = readdir($handle)) !== false) {
        if (!get_show_item($dir, $new_item)) continue;
        if (!get_is_dir($dir, $new_item)) continue;
        $dir_list[$new_item] = $new_item;
    }
    if (is_array($dir_list)) ksort($dir_list);
    return $dir_list;
}
function dir_print($dir_list, $new_dir) {
    $dir_up = dirname($new_dir);
    if ($dir_up == ".") $dir_up = "";
    echo "<TR><TD><A HREF=\"javascript:NewDir('" . $dir_up;
    echo "');\"><IMG border=\"0\" width=\"16\" height=\"16\"";
    echo " align=\"ABSMIDDLE\" src=\"img/_up.png\" ALT=\"\">&nbsp;..</A></TD></TR>\n";
    if (!is_array($dir_list)) return;
    while (list($new_item,) = each($dir_list)) {
        $s_item = $new_item;
        if (strlen($s_item) > 40) $s_item = substr($s_item, 0, 37) . "...";
        echo "<TR><TD><A HREF=\"javascript:NewDir('" . get_rel_item($new_dir, $new_item) . "');\"><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" " . "src=\"img/dir.png\" ALT=\"\">&nbsp;" . $s_item . "</A></TD></TR>\n";
    }
}
function copy_move_items($dir) {
    if (($GLOBALS["permissions"] & 01) != 01) show_error($GLOBALS["error_msg"]["accessfunc"]);
    $first = $GLOBALS['__POST']["first"];
    if ($first == "y") $new_dir = $dir;
    else $new_dir = stripslashes($GLOBALS['__POST']["new_dir"]);
    if ($new_dir == ".") $new_dir = "";
    $cnt = count($GLOBALS['__POST']["selitems"]);
    if ($GLOBALS["action"] != "move") {
        $_img = "img/__copy.png";
    } else {
        $_img = "img/__cut.png";
    }
    if (!isset($GLOBALS['__POST']["confirm"]) || $GLOBALS['__POST']["confirm"] != "true") {
		show_header(($GLOBALS["action"] != "move" ? $GLOBALS["messages"]["actcopyitems"] : $GLOBALS["messages"]["actmoveitems"]));
?>
<script language="JavaScript1.2" type="text/javascript">
    function NewDir(newdir) {
        document.selform.new_dir.value = newdir;
        document.selform.submit();
    }

    function Execute() {
        document.selform.confirm.value = "true";
    }
</script>
<?php
        $s_dir = $dir;
        if (strlen($s_dir) > 40) $s_dir = "..." . substr($s_dir, -37);
        $s_ndir = $new_dir;
        if (strlen($s_ndir) > 40) $s_ndir = "..." . substr($s_ndir, -37);
        echo "<BR><IMG SRC=\"" . $_img . "\" align=\"ABSMIDDLE\" ALT=\"\">&nbsp;";
        echo sprintf(($GLOBALS["action"] != "move" ? $GLOBALS["messages"]["actcopyfrom"] : $GLOBALS["messages"]["actmovefrom"]), $s_dir, $s_ndir);
        echo "<IMG SRC=\"img/__paste.png\" align=\"ABSMIDDLE\" ALT=\"\">\n";
        echo "<BR><BR><FORM name=\"selform\" method=\"post\" action=\"";
        echo make_link("post", $dir, NULL) . "\"><TABLE>\n";
        echo "<INPUT type=\"hidden\" name=\"do_action\" value=\"" . $GLOBALS["action"] . "\">\n";
        echo "<INPUT type=\"hidden\" name=\"confirm\" value=\"false\">\n";
        echo "<INPUT type=\"hidden\" name=\"first\" value=\"n\">\n";
        echo "<INPUT type=\"hidden\" name=\"new_dir\" value=\"" . $new_dir . "\">\n";
        dir_print(dir_list($new_dir), $new_dir);
        echo "</TABLE><BR><TABLE>\n";
        for ($i = 0;$i < $cnt;++$i) {
            $selitem = stripslashes($GLOBALS['__POST']["selitems"][$i]);
            if (isset($GLOBALS['__POST']["newitems"][$i])) {
                $newitem = stripslashes($GLOBALS['__POST']["newitems"][$i]);
                if ($first == "y") $newitem = $selitem;
            } else $newitem = $selitem;
            $s_item = $selitem;
            if (strlen($s_item) > 50) $s_item = substr($s_item, 0, 47) . "...";
            echo "<TR><TD><IMG SRC=\"img/_info.png\" align=\"ABSMIDDLE\" ALT=\"\">";
            echo "<INPUT type=\"hidden\" name=\"selitems[]\" value=\"";
            echo $selitem . "\">&nbsp;" . $s_item . "&nbsp;";
            echo "</TD><TD><INPUT type=\"text\" size=\"25\" name=\"newitems[]\" value=\"";
            echo $newitem . "\"></TD></TR>\n";
        }
        echo "</TABLE><BR><TABLE><TR>\n<TD>";
        echo "<INPUT type=\"submit\" value=\"";
        echo ($GLOBALS["action"] != "move" ? $GLOBALS["messages"]["btncopy"] : $GLOBALS["messages"]["btnmove"]);
        echo "\" onclick=\"javascript:Execute();\" class=\"button\"></TD>\n<TD>";
        echo "<input type=\"button\" value=\"" . $GLOBALS["messages"]["btncancel"];
        echo "\" onClick=\"javascript:location='" . make_link("list", $dir, NULL);
        echo "';\" class=\"button\"></TD>\n</TR></FORM></TABLE><BR>\n";
        return;
    }
    if (!@file_exists(get_abs_dir($new_dir))) show_error($new_dir . ": " . $GLOBALS["error_msg"]["targetexist"]);
    if (!get_show_item($new_dir, "")) show_error($new_dir . ": " . $GLOBALS["error_msg"]["accesstarget"]);
    if (!down_home(get_abs_dir($new_dir))) show_error($new_dir . ": " . $GLOBALS["error_msg"]["targetabovehome"]);
    $err = false;
    for ($i = 0;$i < $cnt;++$i) {
        $tmp = stripslashes($GLOBALS['__POST']["selitems"][$i]);
        $new = basename(stripslashes($GLOBALS['__POST']["newitems"][$i]));
        $abs_item = get_abs_item($dir, $tmp);
        $abs_new_item = get_abs_item($new_dir, $new);
        $items[$i] = $tmp;
        if ($new == "") {
            $error[$i] = $GLOBALS["error_msg"]["miscnoname"];
            $err = true;
            continue;
        }
        if (!@file_exists($abs_item)) {
            $error[$i] = $GLOBALS["error_msg"]["itemexist"];
            $err = true;
            continue;
        }
        if (!get_show_item($dir, $tmp)) {
            $error[$i] = $GLOBALS["error_msg"]["accessitem"];
            $err = true;
            continue;
        }
        if (@file_exists($abs_new_item)) {
            $error[$i] = $GLOBALS["error_msg"]["targetdoesexist"];
            $err = true;
            continue;
        }


		if (eregi($GLOBALS["allowed_file"], $abs_new_item) == false ||
			eregi($GLOBALS["allowed_file"], $abs_item) == false) {
			show_error($GLOBALS["error_msg"]["invalidtype"]);
		}

        if ($GLOBALS["action"] == "copy") {
            if (@is_link($abs_item) || @is_file($abs_item)) {
				$ok = @copy($abs_item, $abs_new_item);
            } elseif (@is_dir($abs_item)) {
				$ok = copy_dir($abs_item, $abs_new_item);
            }
        } else {
			$ok = @rename($abs_item, $abs_new_item);
        }
        if ($ok === false) {
            $error[$i] = ($GLOBALS["action"] == "copy" ? $GLOBALS["error_msg"]["copyitem"] : $GLOBALS["error_msg"]["moveitem"]);
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
} ?>
