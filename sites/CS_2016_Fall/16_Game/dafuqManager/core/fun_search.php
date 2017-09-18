<?php
require_once ('core/ereg_dropin.php');
function find_item($dir, $pat, &$list, $recur) {
    $handle = @opendir(get_abs_dir($dir));
    if ($handle === false) return;
    while (($new_item = readdir($handle)) !== false) {
        if (!@file_exists(get_abs_item($dir, $new_item))) continue;
        if (!get_show_item($dir, $new_item)) continue;
        if (@eregi($pat, $new_item)) $list[] = array($dir, $new_item);
        if (get_is_dir($dir, $new_item) && $recur) {
            find_item(get_rel_item($dir, $new_item), $pat, $list, $recur);
        }
    }
    closedir($handle);
}
function make_list($dir, $item, $subdir) {
    $pat = "^" . str_replace("?", ".", str_replace("*", ".*", str_replace(".", "\.", $item))) . "$";
    find_item($dir, $pat, $list, $subdir);
    if (is_array($list)) sort($list);
    return $list;
}
function print_table($list) {
    if (!is_array($list)) return;
    $cnt = count($list);
    for ($i = 0;$i < $cnt;++$i) {
        $dir = $list[$i][0];
        $item = $list[$i][1];
        $s_dir = $dir;
        if (strlen($s_dir) > 65) $s_dir = substr($s_dir, 0, 62) . "...";
        $s_item = $item;
        if (strlen($s_item) > 45) $s_item = substr($s_item, 0, 42) . "...";
        $link = "";
        $target = "";
        if (get_is_dir($dir, $item)) {
            $img = "dir.png";
            $link = make_link("list", get_rel_item($dir, $item), NULL);
        } else {
            $img = get_mime_type($dir, $item, "img");
            $link = $GLOBALS["home_url"] . "/" . get_rel_item($dir, $item);
            $target = "_blank";
        }
        echo "<TR><TD>" . "<IMG border=\"0\" width=\"16\" height=\"16\" ";
        echo "align=\"ABSMIDDLE\" src=\"img/" . $img . "\" ALT=\"\">&nbsp;";
        echo "<A HREF=\"" . $link . "\" TARGET=\"" . $target . "\">";
        echo $s_item . "</A></TD><TD><A HREF=\"" . make_link("list", $dir, NULL) . "\"> /";
        echo $s_dir . "</A></TD></TR>\n";
    }
}
function search_items($dir) {
    if (isset($GLOBALS['__POST']["searchitem"])) {
        $searchitem = stripslashes($GLOBALS['__POST']["searchitem"]);
        $subdir = (isset($GLOBALS['__POST']["subdir"]) && $GLOBALS['__POST']["subdir"] == "y");
        $list = make_list($dir, $searchitem, $subdir);
    } else {
        $searchitem = NULL;
        $subdir = true;
    }
    $msg = $GLOBALS["messages"]["actsearchresults"];
    if ($searchitem != NULL) $msg.= ": (/" . get_rel_item($dir, $searchitem) . ")";
    show_header($msg);
    echo "<BR><TABLE><FORM name=\"searchform\" action=\"" . make_link("search", $dir, NULL);
    echo "\" method=\"post\">\n<TR><TD><INPUT name=\"searchitem\" type=\"text\" size=\"25\" value=\"";
    echo $searchitem . "\"><INPUT type=\"submit\" value=\"" . $GLOBALS["messages"]["btnsearch"];
    echo "\" class=\"button\">&nbsp;<input type=\"button\" value=\"" . $GLOBALS["messages"]["btnclose"];
    echo "\" onClick=\"javascript:location='" . make_link("list", $dir, NULL);
    echo "';\" class=\"button\"></TD></TR><TR><TD><INPUT type=\"checkbox\" name=\"subdir\" value=\"y\"";
    echo ($subdir ? " checked>" : ">") . $GLOBALS["messages"]["miscsubdirs"] . "</TD></TR></FORM></TABLE>\n";
    if ($searchitem != NULL) {
        echo "<TABLE width=\"95%\"><TR><TD colspan=\"2\"><HR></TD></TR>\n";
        if (count($list) > 0) {
            echo "<TR>\n<TD WIDTH=\"42%\" class=\"header\"><B>" . $GLOBALS["messages"]["nameheader"];
            echo "</B></TD>\n<TD WIDTH=\"58%\" class=\"header\"><B>" . $GLOBALS["messages"]["pathheader"];
            echo "</B></TD></TR>\n<TR><TD colspan=\"2\"><HR></TD></TR>\n";
            print_table($list);
            echo "<TR><TD colspan=\"2\"><HR></TD></TR>\n<TR><TD class=\"header\">" . count($list) . " ";
            echo $GLOBALS["messages"]["miscitems"] . ".</TD><TD class=\"header\"></TD></TR>\n";
        } else {
            echo "<TR><TD>" . $GLOBALS["messages"]["miscnoresult"] . "</TD></TR>";
        }
        echo "<TR><TD colspan=\"2\"><HR></TD></TR></TABLE>\n";
    } ?><script language="JavaScript1.2" type="text/javascript">
<!--
    if(document.searchform) document.searchform.searchitem.focus();
// -->
</script><?php
} ?>
