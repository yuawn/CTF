<?php
require_once ('core/secure.php');
if ($GLOBALS["zip"]) include ("./lib/lib_zip.php");
function zip_items($dir, $name) {
    $cnt = count($GLOBALS['__POST']["selitems"]);
    $abs_dir = get_abs_dir($dir);
    $zipfile = new ZipFile();
    for ($i = 0;$i < $cnt;++$i) {
        $selitem = stripslashes($GLOBALS['__POST']["selitems"][$i]);
        $selitem = sanitize($selitem);
        $selitem = iconv('ascii', 'ascii//ignore', $selitem);
        $path = realpath(sprintf('%s/%s', $abs_dir, $selitem));
        if (file_in_web($path) && file_exists($path) && !$zipfile->add($abs_dir, $selitem)) {
            show_error($selitem . ": Failed adding item.");
        }
    }
    $contents = $zipfile->contents();
    header('Content-Disposition: attachment; filename="' . $name . '"');
    header('Cache-Control: no-cache, must-revalidate');
    header('Pragma: no-cache');
    header('Content-Transfer-Encoding: binary');
    header('Content-Length: ' . strlen($contents));
    echo $contents;
    die;
}
function tar_items($dir, $name) {
	show_error($GLOBALS["error_msg"]["notimplemented"]);
}
function tgz_items($dir, $name) {
	show_error($GLOBALS["error_msg"]["notimplemented"]);
}
function archive_items($dir) {
    if (($GLOBALS["permissions"] & 01) != 01) show_error($GLOBALS["error_msg"]["accessfunc"]);
    if (!$GLOBALS["zip"] && !$GLOBALS["tar"] && !$GLOBALS["tgz"]) show_error($GLOBALS["error_msg"]["miscnofunc"]);
    if (isset($GLOBALS['__POST']["name"])) {
        $name = basename(stripslashes($GLOBALS['__POST']["name"]));
        if ($name == "") show_error($GLOBALS["error_msg"]["miscnoname"]);
        switch ($GLOBALS['__POST']["type"]) {
            case "zip":
                zip_items($dir, $name);
            break;
            case "tar":
                tar_items($dir, $name);
            break;
            default:
                tgz_items($dir, $name);
        }
        header("Location: " . make_link("list", $dir, NULL));
    }
    show_header($GLOBALS["messages"]["actarchive"]);
    echo "<BR><FORM name=\"archform\" method=\"post\" action=\"" . make_link("arch", $dir, NULL) . "\">\n";
    $cnt = count($GLOBALS['__POST']["selitems"]);
    for ($i = 0;$i < $cnt;++$i) {
        echo "<INPUT type=\"hidden\" name=\"selitems[]\" value=\"" . stripslashes($GLOBALS['__POST']["selitems"][$i]) . "\">\n";
    }
    echo "<TABLE width=\"300\"><TR><TD>" . $GLOBALS["messages"]["nameheader"] . ":</TD><TD align=\"right\">";
    echo "<INPUT type=\"text\" name=\"name\" size=\"25\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["typeheader"] . ":</TD><TD align=\"right\"><SELECT name=\"type\">\n";
    if ($GLOBALS["zip"]) echo "<OPTION value=\"zip\">Zip</OPTION>\n";
    if ($GLOBALS["tar"]) echo "<OPTION value=\"tar\">Tar</OPTION>\n";
    if ($GLOBALS["tgz"]) echo "<OPTION value=\"tgz\">TGz</OPTION>\n";
    echo "</SELECT></TD></TR>";
    echo "<TR><TD></TD><TD align=\"right\"><INPUT type=\"submit\" value=\"" . $GLOBALS["messages"]["btncreate"] . "\" class=\"button\">\n";
    echo "<input type=\"button\" value=\"" . $GLOBALS["messages"]["btncancel"];
    echo "\" onClick=\"javascript:location='" . make_link("list", $dir, NULL) . "';\" class=\"button\">\n</TD></TR></FORM></TABLE><BR>\n"; ?><script language="JavaScript1.2" type="text/javascript">
<!--
    if(document.archform) document.archform.name.focus();
// -->
</script><?php
} ?>
