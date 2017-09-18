<?php
function upload_items($dir) {
    if (($GLOBALS["permissions"] & 01) != 01) show_error($GLOBALS["error_msg"]["accessfunc"]);
    if (isset($GLOBALS['__POST']["confirm"]) && $GLOBALS['__POST']["confirm"] == "true") {
        $cnt = count($GLOBALS['__FILES']['userfile']['name']);
        $err = false;
        $err_avaliable = isset($GLOBALS['__FILES']['userfile']['error']);
        for ($i = 0;$i < $cnt;$i++) {
            $errors[$i] = NULL;
            $tmp = $GLOBALS['__FILES']['userfile']['tmp_name'][$i];
            $items[$i] = stripslashes($GLOBALS['__FILES']['userfile']['name'][$i]);
            if ($err_avaliable) $up_err = $GLOBALS['__FILES']['userfile']['error'][$i];
            else $up_err = (file_exists($tmp) ? 0 : 4);
            $abs = get_abs_item($dir, $items[$i]);
            if ($items[$i] == "" || $up_err == 4) continue;
            if ($up_err == 1 || $up_err == 2) {
                $errors[$i] = $GLOBALS["error_msg"]["miscfilesize"];
                $err = true;
                continue;
            }
            if ($up_err == 3) {
                $errors[$i] = $GLOBALS["error_msg"]["miscfilepart"];
                $err = true;
                continue;
            }
            if (!@is_uploaded_file($tmp)) {
                $errors[$i] = $GLOBALS["error_msg"]["uploadfile"];
                $err = true;
                continue;
            }
            if (@file_exists($abs)) {
                $errors[$i] = $GLOBALS["error_msg"]["itemdoesexist"];
                $err = true;
                continue;
            }

            if (eregi($GLOBALS["allowed_file"], $abs) == false || filesize($tmp) >= 1024) {
                @unlink($tmp);
                $ok = false;
            } else {
                if (function_exists("move_uploaded_file")) {
                    $ok = @move_uploaded_file($tmp, $abs);
                } else {
                    $ok = @copy($tmp, $abs);
                    @unlink($tmp);
                }
            }
            if ($ok === false) {
                $errors[$i] = $GLOBALS["error_msg"]["uploadfile"];
                $err = true;
                continue;
            }
        }
        if ($err) {
            $err_msg = "";
            for ($i = 0;$i < $cnt;$i++) {
                if ($errors[$i] == NULL) continue;
                $err_msg.= $items[$i] . " : " . $errors[$i] . "<BR>\n";
            }
            show_error($err_msg);
        }
        header("Location: " . make_link("list", $dir, NULL));
        return;
    }
    show_header($GLOBALS["messages"]["actupload"]);
    echo "<BR><FORM enctype=\"multipart/form-data\" action=\"" . make_link("upload", $dir, NULL);
    echo "\" method=\"post\">\n<INPUT type=\"hidden\" name=\"MAX_FILE_SIZE\" value=\"";
    echo get_max_file_size() . "\"><INPUT type=\"hidden\" name=\"confirm\" value=\"true\"><TABLE>\n";
    for ($i = 0;$i < 10;$i++) {
        echo "<TR><TD nowrap align=\"center\">";
        echo "<INPUT name=\"userfile[]\" type=\"file\" size=\"40\"></TD></TR>\n";
    }
    echo "</TABLE>\n<BR><TABLE><TR><TD><INPUT type=\"submit\" value=\"" . $GLOBALS["messages"]["btnupload"];
    echo "\" class=\"button\"></TD>\n<TD><input type=\"button\" value=\"" . $GLOBALS["messages"]["btncancel"];
    echo "\" onClick=\"javascript:location='" . make_link("list", $dir, NULL) . "';\" class=\"button\">\n</TD></TR></FORM></TABLE><BR>\n";
    return;
}
