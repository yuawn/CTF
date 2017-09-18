<?php
require_once ('core/ereg_dropin.php');
require_once ('core/secure.php');
function savefile($dir, $file_name) {
    $file_name = sanitize($file_name);
    if (!file_in_web($file_name)) {
        show_error(basename($file_name) . ": " . $GLOBALS["error_msg"]["savefile"]);
    }
    $code = stripslashes($GLOBALS['__POST']["code"]);
    $fp = @fopen($file_name, "w");
    if ($fp === false) show_error(basename($file_name) . ": " . $GLOBALS["error_msg"]["savefile"]);
    fputs($fp, $code);
    @fclose($fp);
}
function edit_file($dir, $item) {
    if (($GLOBALS["permissions"] & 01) != 01) show_error($GLOBALS["error_msg"]["accessfunc"]);
    if (!get_is_file($dir, $item)) show_error($item . ": " . $GLOBALS["error_msg"]["fileexist"]);
    if (!get_show_item($dir, $item)) show_error($item . ": " . $GLOBALS["error_msg"]["accessfile"]);
    $fname = get_abs_item($dir, $item);
    if (!file_in_web($fname)) show_error($GLOBALS["error_msg"]["accessfile"]);
    if (isset($GLOBALS['__POST']["dosave"]) && $GLOBALS['__POST']["dosave"] == "yes") {
        $item = basename(stripslashes($GLOBALS['__POST']["fname"]));
        $fname2 = get_abs_item($dir, $item);
        if (!isset($item) || $item == "") show_error($GLOBALS["error_msg"]["miscnoname"]);
        if ($fname != $fname2 && @file_exists($fname2)) show_error($item . ": " . $GLOBALS["error_msg"]["itemdoesexist"]);
        savefile($dir, $fname2);
        $fname = $fname2;
    }
    $fp = @fopen($fname, "r");
    if ($fp === false) show_error($item . ": " . $GLOBALS["error_msg"]["openfile"]);
    $s_item = get_rel_item($dir, $item);
    if (strlen($s_item) > 50) $s_item = "..." . substr($s_item, -47);
    show_header($GLOBALS["messages"]["actedit"] . ": /" . $s_item); ?><script language="JavaScript1.2" type="text/javascript">
<!--
    function chwrap() {
        if(document.editfrm.wrap.checked) {
            document.editfrm.code.wrap="soft";
        } else {
            document.editfrm.code.wrap="off";
        }
    }
// -->
</script><?php
    echo "<BR><FORM name=\"editfrm\" method=\"post\" action=\"" . make_link("edit", $dir, $item) . "\">\n";
    echo "<input type=\"hidden\" name=\"dosave\" value=\"yes\">\n";
    echo "<TEXTAREA NAME=\"code\" rows=\"25\" cols=\"120\" wrap=\"off\">";
    $buffer = "";
    while (!feof($fp)) {
        $buffer.= fgets($fp, 4096);
    }
    @fclose($fp);
    echo htmlspecialchars($buffer);
    echo "</TEXTAREA><BR>\n<TABLE><TR><TD>Wordwrap: (IE only)</TD><TD><INPUT type=\"checkbox\" name=\"wrap\" ";
    echo "onClick=\"javascript:chwrap();\" value=\"1\"></TD></TR></TABLE><BR>\n";
    echo "<TABLE><TR><TD><INPUT type=\"text\" name=\"fname\" value=\"" . $item . "\"></TD>";
    echo "<TD><input type=\"submit\" value=\"" . $GLOBALS["messages"]["btnsave"];
    echo "\" class=\"button\"></TD>\n<TD><input type=\"reset\" value=\"" . $GLOBALS["messages"]["btnreset"] . "\"></TD>\n<TD>";
    echo "<input type=\"button\" value=\"" . $GLOBALS["messages"]["btnclose"] . "\" onClick=\"javascript:location='";
    echo make_link("list", $dir, NULL) . "';\" class=\"button\"></TD></TR></FORM></TABLE><BR>\n"; ?><script language="JavaScript1.2" type="text/javascript">
<!--
    if(document.editfrm) document.editfrm.code.focus();
// -->
</script><?php
} ?>
