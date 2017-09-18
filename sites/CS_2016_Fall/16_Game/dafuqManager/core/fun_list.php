<?php
function make_list($_list1, $_list2) {
    $list = array();
    if ($GLOBALS["srt"] == "yes") {
        $list1 = $_list1;
        $list2 = $_list2;
    } else {
        $list1 = $_list2;
        $list2 = $_list1;
    }
    if (is_array($list1)) {
        while (list($key, $val) = each($list1)) {
            $list[$key] = $val;
        }
    }
    if (is_array($list2)) {
        while (list($key, $val) = each($list2)) {
            $list[$key] = $val;
        }
    }
    return $list;
}
function make_tables($dir, &$dir_list, &$file_list, &$tot_file_size, &$num_items) {
    $tot_file_size = $num_items = 0;
    $handle = @opendir(get_abs_dir($dir));
    if ($handle === false) show_error($dir . ": " . $GLOBALS["error_msg"]["opendir"]);
    while (($new_item = readdir($handle)) !== false) {
        $abs_new_item = get_abs_item($dir, $new_item);
        if (!@file_exists($abs_new_item)) show_error($dir . ": " . $GLOBALS["error_msg"]["readdir"]);
        if (!get_show_item($dir, $new_item)) continue;
        $new_file_size = filesize($abs_new_item);
        $tot_file_size+= $new_file_size;
        $num_items++;
        if (get_is_dir($dir, $new_item)) {
            if ($GLOBALS["order"] == "mod") {
                $dir_list[$new_item] = @filemtime($abs_new_item);
            } else {
                $dir_list[$new_item] = $new_item;
            }
        } else {
            if ($GLOBALS["order"] == "size") {
                $file_list[$new_item] = $new_file_size;
            } elseif ($GLOBALS["order"] == "mod") {
                $file_list[$new_item] = @filemtime($abs_new_item);
            } elseif ($GLOBALS["order"] == "type") {
                $file_list[$new_item] = get_mime_type($dir, $new_item, "type");
            } else {
                $file_list[$new_item] = $new_item;
            }
        }
    }
    closedir($handle);
    if (is_array($dir_list)) {
        if ($GLOBALS["order"] == "mod") {
            if ($GLOBALS["srt"] == "yes") arsort($dir_list);
            else asort($dir_list);
        } else {
            if ($GLOBALS["srt"] == "yes") ksort($dir_list);
            else krsort($dir_list);
        }
    }
    if (is_array($file_list)) {
        if ($GLOBALS["order"] == "mod") {
            if ($GLOBALS["srt"] == "yes") arsort($file_list);
            else asort($file_list);
        } elseif ($GLOBALS["order"] == "size" || $GLOBALS["order"] == "type") {
            if ($GLOBALS["srt"] == "yes") asort($file_list);
            else arsort($file_list);
        } else {
            if ($GLOBALS["srt"] == "yes") ksort($file_list);
            else krsort($file_list);
        }
    }
}
function print_table($dir, $list, $allow) {
    if (!is_array($list)) return;
    while (list($item,) = each($list)) {
        $abs_item = get_abs_item($dir, $item);
        $target = "";
        if (is_dir($abs_item)) {
            $link = make_link("list", get_rel_item($dir, $item), NULL);
        } else {
            $link = $GLOBALS["home_url"] . "/" . get_rel_item($dir, $item);
            $target = "_blank";
        }
        echo "<TR class=\"rowdata\"><TD><INPUT TYPE=\"checkbox\" name=\"selitems[]\" value=\"";
        echo htmlspecialchars($item) . "\" onclick=\"javascript:Toggle(this);\"></TD>\n";
        echo "<TD nowrap>";
        echo "<A HREF=\"" . $link . "\" TARGET=\"" . $target . "\">";
        echo "<IMG border=\"0\" width=\"16\" height=\"16\" ";
        echo "align=\"ABSMIDDLE\" src=\"img/" . get_mime_type($dir, $item, "img") . "\" ALT=\"\">&nbsp;";
        $s_item = $item;
        if (strlen($s_item) > 50) $s_item = substr($s_item, 0, 47) . "...";
        echo htmlspecialchars($s_item) . "</A></TD>\n";
        echo "<TD>" . parse_file_size(get_file_size($dir, $item)) . "</TD>\n";
        echo "<TD>" . get_mime_type($dir, $item, "type") . "</TD>\n";
        echo "<TD>" . parse_file_date(get_file_date($dir, $item)) . "</TD>\n";
        echo "<TD>";
        if ($allow) {
            echo "<A HREF=\"" . make_link("chmod", $dir, $item) . "\" TITLE=\"";
            echo $GLOBALS["messages"]["permlink"] . "\">";
        }
        echo parse_file_type($dir, $item) . parse_file_perms(get_file_perms($dir, $item));
        if ($allow) echo "</A>";
        echo "</TD>\n";
        echo "<TD>\n<TABLE>\n";
        if (get_is_editable($dir, $item)) {
            if ($allow) {
                echo "<TD><A HREF=\"" . make_link("edit", $dir, $item) . "\">";
                echo "<IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
                echo "src=\"img/_edit.png\" ALT=\"" . $GLOBALS["messages"]["editlink"] . "\" TITLE=\"";
                echo $GLOBALS["messages"]["editlink"] . "\"></A></TD>\n";
            } else {
                echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
                echo "src=\"img/_edit_.png\" ALT=\"" . $GLOBALS["messages"]["editlink"] . "\" TITLE=\"";
                echo $GLOBALS["messages"]["editlink"] . "\"></TD>\n";
            }
        } else {
            echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
            echo "src=\"img/_.png\" ALT=\"\"></TD>\n";
        }
        if (get_is_file($dir, $item)) {
            if ($allow) {
                echo "<TD><A HREF=\"" . make_link("download", $dir, $item) . "\">";
                echo "<IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
                echo "src=\"img/_download.png\" ALT=\"" . $GLOBALS["messages"]["downlink"];
                echo "\" TITLE=\"" . $GLOBALS["messages"]["downlink"] . "\"></A></TD>\n";
            } else if (!$allow) {
                echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
                echo "src=\"img/_download_.png\" ALT=\"" . $GLOBALS["messages"]["downlink"];
                echo "\" TITLE=\"" . $GLOBALS["messages"]["downlink"] . "\"></TD>\n";
            }
        } else {
            echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
            echo "src=\"img/_.png\" ALT=\"\"></TD>\n";
        }
        echo "</TABLE>\n</TD></TR>\n";
    }
}
function list_dir($dir) {
    $allow = ($GLOBALS["permissions"] & 01) == 01;
    $admin = ((($GLOBALS["permissions"] & 04) == 04) || (($GLOBALS["permissions"] & 02) == 02));
    $dir_up = dirname($dir);
    if ($dir_up == ".") $dir_up = "";
    if (!get_show_item($dir_up, basename($dir))) show_error($dir . " : " . $GLOBALS["error_msg"]["accessdir"]);
    make_tables($dir, $dir_list, $file_list, $tot_file_size, $num_items);
    $s_dir = $dir;
    if (strlen($s_dir) > 50) $s_dir = "..." . substr($s_dir, -47);
    show_header($GLOBALS["messages"]["actdir"] . ": /" . get_rel_item("", $s_dir));
    include "./core/javascript.php";
    $_img = "&nbsp;<IMG width=\"10\" height=\"10\" border=\"0\" align=\"ABSMIDDLE\" src=\"img/";
    if ($GLOBALS["srt"] == "yes") {
        $_srt = "no";
        $_img.= "_arrowup.png\" ALT=\"^\">";
    } else {
        $_srt = "yes";
        $_img.= "_arrowdown.png\" ALT=\"v\">";
    }
    echo "<BR><TABLE width=\"95%\" class=\"toolbar\"><TR><TD><TABLE><TR>\n";
    echo "<TD><A HREF=\"" . make_link("list", $dir_up, NULL) . "\">";
    echo "<IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" src=\"img/_up.png\" ";
    echo "ALT=\"" . $GLOBALS["messages"]["uplink"] . "\" TITLE=\"" . $GLOBALS["messages"]["uplink"] . "\">{$GLOBALS['messages']['uplink']}</A></TD>\n";
    echo "<TD><A HREF=\"" . make_link("list", NULL, NULL) . "\">";
    echo "<IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" src=\"img/_home.png\" ";
    echo "ALT=\"" . $GLOBALS["messages"]["homelink"] . "\" TITLE=\"" . $GLOBALS["messages"]["homelink"] . "\">{$GLOBALS['messages']['homelink']}</A></TD>\n";
    echo "<TD><A HREF=\"javascript:location.reload();\"><IMG border=\"0\" width=\"16\" height=\"16\" ";
    echo "align=\"ABSMIDDLE\" src=\"img/_refresh.png\" ALT=\"" . $GLOBALS["messages"]["reloadlink"];
    echo "\" TITLE=\"" . $GLOBALS["messages"]["reloadlink"] . "\">{$GLOBALS['messages']['reloadlink']}</A></TD>\n";
    echo "<TD><A HREF=\"" . make_link("search", $dir, NULL) . "\">";
    echo "<IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" src=\"img/_search.png\" ";
    echo "ALT=\"" . $GLOBALS["messages"]["searchlink"] . "\" TITLE=\"" . $GLOBALS["messages"]["searchlink"];
    echo "\">" . $GLOBALS["messages"]["searchlink"] . "</A></TD>\n";
    echo "<TD class=\"splitter\"></TD>";
    if ($allow) {
        echo "<TD><A HREF=\"javascript:Copy();\"><IMG border=\"0\" width=\"16\" height=\"16\" ";
        echo "align=\"ABSMIDDLE\" src=\"img/_copy.png\" ALT=\"" . $GLOBALS["messages"]["copylink"];
        echo "\" TITLE=\"" . $GLOBALS["messages"]["copylink"] . "\">" . $GLOBALS["messages"]["copylink"] . "</A></TD>\n";
        echo "<TD><A HREF=\"javascript:Move();\"><IMG border=\"0\" width=\"16\" height=\"16\" ";
        echo "align=\"ABSMIDDLE\" src=\"img/_move.png\" ALT=\"" . $GLOBALS["messages"]["movelink"];
        echo "\" TITLE=\"" . $GLOBALS["messages"]["movelink"] . "\">" . $GLOBALS["messages"]["movelink"] . "</A></TD>\n";
        echo "<TD><A HREF=\"javascript:Delete();\"><IMG border=\"0\" width=\"16\" height=\"16\" ";
        echo "align=\"ABSMIDDLE\" src=\"img/_delete.png\" ALT=\"" . $GLOBALS["messages"]["dellink"];
        echo "\" TITLE=\"" . $GLOBALS["messages"]["dellink"] . "\">" . $GLOBALS["messages"]["dellink"] . "</A></TD>\n";
        if (get_cfg_var("file_uploads")) {
            echo "<TD><A HREF=\"" . make_link("upload", $dir, NULL) . "\">";
            echo "<IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
            echo "src=\"img/_upload.png\" ALT=\"" . $GLOBALS["messages"]["uploadlink"];
            echo "\" TITLE=\"" . $GLOBALS["messages"]["uploadlink"] . "\">" . $GLOBALS["messages"]["uploadlink"] . "</A></TD>\n";
        } else {
            echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
            echo "src=\"img/_upload_.png\" ALT=\"" . $GLOBALS["messages"]["uploadlink"];
            echo "\" TITLE=\"" . $GLOBALS["messages"]["uploadlink"] . "\">" . $GLOBALS["messages"]["uploadlink"] . "</TD>\n";
        }
        if ($GLOBALS["zip"] || $GLOBALS["tar"] || $GLOBALS["tgz"]) {
            echo "<!--<TD><A HREF=\"javascript:Archive();\"><IMG border=\"0\" width=\"16\" height=\"16\" ";
            echo "align=\"ABSMIDDLE\" src=\"img/_archive.png\" ALT=\"" . $GLOBALS["messages"]["comprlink"];
            echo "\" TITLE=\"" . $GLOBALS["messages"]["comprlink"] . "\">" . $GLOBALS["messages"]["comprlink"] . "</A></TD>-->\n";
        }
    } else {
        echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
        echo "src=\"img/_copy_.png\" ALT=\"" . $GLOBALS["messages"]["copylink"] . "\" TITLE=\"";
        echo $GLOBALS["messages"]["copylink"] . "\">" . $GLOBALS["messages"]["copylink"] . "</TD>\n";
        echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
        echo "src=\"img/_move_.png\" ALT=\"" . $GLOBALS["messages"]["movelink"] . "\" TITLE=\"";
        echo $GLOBALS["messages"]["movelink"] . "\">" . $GLOBALS["messages"]["movelink"] . "</TD>\n";
        echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
        echo "src=\"img/_delete_.png\" ALT=\"" . $GLOBALS["messages"]["dellink"] . "\" TITLE=\"";
        echo $GLOBALS["messages"]["dellink"] . "\">" . $GLOBALS["messages"]["dellink"] . "</TD>\n";
        echo "<TD><IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
        echo "src=\"img/_upload_.png\" ALT=\"" . $GLOBALS["messages"]["uplink"];
        echo "\" TITLE=\"" . $GLOBALS["messages"]["uplink"] . "\">" . $GLOBALS["messages"]["uplink"] . "</TD>\n";
    }
    if ($GLOBALS["require_login"]) {
        echo "<TD class=\"splitter\"></TD>";
        if ($admin) {
            echo "<TD><A HREF=\"" . make_link("admin", $dir, NULL) . "\">";
            echo "<IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
            echo "src=\"img/_admin.png\" ALT=\"" . $GLOBALS["messages"]["adminlink"] . "\" TITLE=\"";
            echo $GLOBALS["messages"]["adminlink"] . "\">" . $GLOBALS["messages"]["adminlink"] . "</A></TD>\n";
        }
        echo "<TD><A HREF=\"" . make_link("logout", NULL, NULL) . "\">";
        echo "<IMG border=\"0\" width=\"16\" height=\"16\" align=\"ABSMIDDLE\" ";
        echo "src=\"img/_logout.png\" ALT=\"" . $GLOBALS["messages"]["logoutlink"] . "\" TITLE=\"";
        echo $GLOBALS["messages"]["logoutlink"] . "\">" . $GLOBALS["messages"]["logoutlink"] . "</A></TD>\n";
    }
    echo "</TR></TABLE></TD>\n";
    if ($allow) {
        echo "<TD align=\"right\"><TABLE><FORM action=\"" . make_link("mkitem", $dir, NULL) . "\" method=\"post\">\n<TR><TD>";
        echo "<SELECT name=\"mktype\"><option value=\"file\">" . $GLOBALS["mimes"]["file"] . "</option>";
        echo "<option value=\"dir\">" . $GLOBALS["mimes"]["dir"] . "</option></SELECT>\n";
        echo "<INPUT name=\"mkname\" type=\"text\" size=\"15\">";
        echo "<INPUT type=\"submit\" value=\"" . $GLOBALS["messages"]["btncreate"];
        echo "\" class=\"button\"></TD></TR></FORM></TABLE></TD>\n";
    }
    echo "</TR></TABLE>\n";
    echo "<TABLE class=\"files\" WIDTH=\"95%\"><FORM name=\"selform\" method=\"POST\" action=\"" . make_link("post", $dir, NULL) . "\">\n";
    echo "<INPUT type=\"hidden\" name=\"do_action\"><INPUT type=\"hidden\" name=\"first\" value=\"y\">\n";
    echo "<TR class=\"header\"><TD WIDTH=\"2%\" class=\"header\">\n";
    echo "<INPUT TYPE=\"checkbox\" name=\"toggleAllC\" onclick=\"javascript:ToggleAll(this);\"></TD>\n";
    echo "<TD WIDTH=\"44%\" class=\"header\"><B>\n";
    if ($GLOBALS["order"] == "name") $new_srt = $_srt;
    else $new_srt = "yes";
    echo "<A href=\"" . make_link("list", $dir, NULL, "name", $new_srt) . "\">" . $GLOBALS["messages"]["nameheader"];
    if ($GLOBALS["order"] == "name") echo $_img;
    echo "</A></B></TD>\n<TD WIDTH=\"10%\" class=\"header\"><B>";
    if ($GLOBALS["order"] == "size") $new_srt = $_srt;
    else $new_srt = "yes";
    echo "<A href=\"" . make_link("list", $dir, NULL, "size", $new_srt) . "\">" . $GLOBALS["messages"]["sizeheader"];
    if ($GLOBALS["order"] == "size") echo $_img;
    echo "</A></B></TD>\n<TD WIDTH=\"16%\" class=\"header\"><B>";
    if ($GLOBALS["order"] == "type") $new_srt = $_srt;
    else $new_srt = "yes";
    echo "<A href=\"" . make_link("list", $dir, NULL, "type", $new_srt) . "\">" . $GLOBALS["messages"]["typeheader"];
    if ($GLOBALS["order"] == "type") echo $_img;
    echo "</A></B></TD>\n<TD WIDTH=\"14%\" class=\"header\"><B>";
    if ($GLOBALS["order"] == "mod") $new_srt = $_srt;
    else $new_srt = "yes";
    echo "<A href=\"" . make_link("list", $dir, NULL, "mod", $new_srt) . "\">" . $GLOBALS["messages"]["modifheader"];
    if ($GLOBALS["order"] == "mod") echo $_img;
    echo "</A></B></TD><TD WIDTH=\"8%\" class=\"header\"><B>" . $GLOBALS["messages"]["permheader"] . "</B>\n";
    echo "</TD><TD WIDTH=\"6%\" class=\"header\"><B>" . $GLOBALS["messages"]["actionheader"] . "</B></TD></TR>\n";
    print_table($dir, make_list($dir_list, $file_list), $allow);
    echo "<TR class=\"footer\">\n<TD class=\"header\"></TD>";
    echo "<TD class=\"header\">" . $num_items . " " . $GLOBALS["messages"]["miscitems"] . " (";
    if (function_exists("disk_free_space")) {
        $free = parse_file_size(disk_free_space(get_abs_dir($dir)));
    } elseif (function_exists("diskfreespace")) {
        $free = parse_file_size(diskfreespace(get_abs_dir($dir)));
    } else $free = "?";
    echo $GLOBALS["messages"]["miscfree"] . ": " . $free . ")</TD>\n";
    echo "<TD class=\"header\">" . parse_file_size($tot_file_size) . "</TD>\n";
    for ($i = 0;$i < 4;++$i) echo "<TD class=\"header\"></TD>";
    echo "</FORM></TABLE>\n"; ?><script language="JavaScript1.2" type="text/javascript">
<!--
    // Uncheck all items (to avoid problems with new items)
    var ml = document.selform;
    var len = ml.elements.length;
    for(var i=0; i<len; ++i) {
        var e = ml.elements[i];
        if(e.name == "selitems[]" && e.checked == true) {
            e.checked=false;
        }
    }
// -->
</script><?php
}
