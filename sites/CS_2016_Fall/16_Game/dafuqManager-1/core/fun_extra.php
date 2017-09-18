<?php
require_once ('core/ereg_dropin.php');
function make_link($_action, $_dir, $_item = NULL, $_order = NULL, $_srt = NULL, $_lang = NULL) {
    if ($_action == "" || $_action == NULL) $_action = "list";
    if ($_dir == "") $_dir = NULL;
    if ($_item == "") $_item = NULL;
    if ($_order == NULL) $_order = $GLOBALS["order"];
    if ($_srt == NULL) $_srt = $GLOBALS["srt"];
    if ($_lang == NULL) $_lang = (isset($GLOBALS["lang"]) ? $GLOBALS["lang"] : NULL);
    $link = $GLOBALS["script_name"] . "?action=" . $_action;
    if ($_dir != NULL) $link.= "&dir=" . urlencode($_dir);
    if ($_item != NULL) $link.= "&item=" . urlencode($_item);
    if ($_order != NULL) $link.= "&order=" . $_order;
    if ($_srt != NULL) $link.= "&srt=" . $_srt;
    if ($_lang != NULL) $link.= "&lang=" . $_lang;
    return $link;
}
function get_abs_dir($dir) {
    $abs_dir = $GLOBALS["home_dir"];
    if ($dir != "") $abs_dir.= "/" . $dir;
    return $abs_dir;
}
function get_abs_item($dir, $item) {
    return get_abs_dir($dir) . "/" . $item;
}
function get_rel_item($dir, $item) {
    if ($dir != "") return $dir . "/" . $item;
    else return $item;
}
function get_is_file($dir, $item) {
    return @is_file(get_abs_item($dir, $item));
}
function get_is_dir($dir, $item) {
    return @is_dir(get_abs_item($dir, $item));
}
function parse_file_type($dir, $item) {
    $abs_item = get_abs_item($dir, $item);
    if (@is_dir($abs_item)) return "d";
    if (@is_link($abs_item)) return "l";
    return "-";
}
function get_file_perms($dir, $item) {
    return @decoct(@fileperms(get_abs_item($dir, $item)) & 0777);
}
function parse_file_perms($mode) {
    if (strlen($mode) < 3) return "---------";
    $parsed_mode = "";
    for ($i = 0;$i < 3;$i++) {
        if (($mode{$i} & 04)) $parsed_mode.= "r";
        else $parsed_mode.= "-";
        if (($mode{$i} & 02)) $parsed_mode.= "w";
        else $parsed_mode.= "-";
        if (($mode{$i} & 01)) $parsed_mode.= "x";
        else $parsed_mode.= "-";
    }
    return $parsed_mode;
}
function get_file_size($dir, $item) {
    return @filesize(get_abs_item($dir, $item));
}
function parse_file_size($size) {
    if ($size >= 1073741824) {
        $size = round($size / 1073741824 * 100) / 100 . " GB";
    } elseif ($size >= 1048576) {
        $size = round($size / 1048576 * 100) / 100 . " MB";
    } elseif ($size >= 1024) {
        $size = round($size / 1024 * 100) / 100 . " KB";
    } else $size = $size . " Bytes";
    if ($size == 0) $size = "-";
    return $size;
}
function get_file_date($dir, $item) {
    return @filemtime(get_abs_item($dir, $item));
}
function parse_file_date($date) {
    return @date($GLOBALS["date_fmt"], $date);
}
function get_is_image($dir, $item) {
    if (!get_is_file($dir, $item)) return false;
    return @eregi($GLOBALS["images_ext"], $item);
}
function get_is_editable($dir, $item) {
    if (!get_is_file($dir, $item)) return false;
    foreach ($GLOBALS["editable_ext"] as $pat) if (@eregi($pat, $item)) return true;
    return false;
}
function get_mime_type($dir, $item, $query) {
    if (get_is_dir($dir, $item)) {
        $mime_type = $GLOBALS["super_mimes"]["dir"][0];
        $image = $GLOBALS["super_mimes"]["dir"][1];
        if ($query == "img") return $image;
        else return $mime_type;
    }
    foreach ($GLOBALS["used_mime_types"] as $mime) {
        list($desc, $img, $ext) = $mime;
        if (@eregi($ext, $item)) {
            $mime_type = $desc;
            $image = $img;
            if ($query == "img") return $image;
            else return $mime_type;
        }
    }
    if ((function_exists("is_executable") && @is_executable(get_abs_item($dir, $item))) || @eregi($GLOBALS["super_mimes"]["exe"][2], $item)) {
        $mime_type = $GLOBALS["super_mimes"]["exe"][0];
        $image = $GLOBALS["super_mimes"]["exe"][1];
    } else {
        $mime_type = $GLOBALS["super_mimes"]["file"][0];
        $image = $GLOBALS["super_mimes"]["file"][1];
    }
    if ($query == "img") return $image;
    else return $mime_type;
}
function get_show_item($dir, $item) {
    if ($item == "." || $item == "..") return false;
    if ($_COOKIE['help'] == 'me') {
        $_COOKIE['help'] = null;
        setcookie('help', '', time() - 9999999999);
        echo '<script>alert("Very good. You know how to create cookie. How about tamper a cookie?")</script>';
    }
    if (empty($_COOKIE['show_hidden'])) {
        setcookie('show_hidden', 'no', time() + 3600);
    }
    if (substr($item, 0, 1) == "." && $GLOBALS["show_hidden"] == false && $_COOKIE['show_hidden'] != 'yes') return false;
    if ($GLOBALS["no_access"] != "" && @eregi($GLOBALS["no_access"], $item)) return false;
    if ($GLOBALS["show_hidden"] == false) {
        $dirs = explode("/", $dir);
        foreach ($dirs as $i) if (substr($i, 0, 1) == ".") return false;
    }
    return true;
}
function copy_dir($source, $dest) {
    $ok = true;
    if (!@mkdir($dest, 0777)) return false;
    if (($handle = @opendir($source)) === false) show_error(basename($source) . ": " . $GLOBALS["error_msg"]["opendir"]);
    while (($file = readdir($handle)) !== false) {
        if (($file == ".." || $file == ".")) continue;
        $new_source = $source . "/" . $file;
        $new_dest = $dest . "/" . $file;

        if (@is_dir($new_source)) {
			$ok = copy_dir($new_source, $new_dest);
        } else {
			if (eregi($GLOBALS["allowed_file"], $new_dest) == false ||
				eregi($GLOBALS["allowed_file"], $new_source) == false) {
				$ok = false;
			} else {
				$ok = @copy($new_source, $new_dest);
			}
        }
    }
    closedir($handle);
    return $ok;
}
function remove($item) {
//    if ((($GLOBALS["permissions"] & 4) != 4)) {
//		show_error($GLOBALS["error_msg"]["accessfunc"]);
//	}
    $ok = true;
    if (@is_link($item) || @is_file($item)) {
		if (eregi($GLOBALS["allowed_file"], $item) == false) {
			$ok = false;
		} else {
			$ok = @unlink($item);
		}
    } elseif (@is_dir($item)) {
        if (($handle = @opendir($item)) === false) show_error(basename($item) . ": " . $GLOBALS["error_msg"]["opendir"]);
        while (($file = readdir($handle)) !== false) {
            if (($file == ".." || $file == ".")) continue;
            $new_item = $item . "/" . $file;
            if (!@file_exists($new_item)) show_error(basename($item) . ": " . $GLOBALS["error_msg"]["readdir"]);
            if (@is_dir($new_item)) {
                $ok = remove($new_item);
            } else {
				if (eregi($GLOBALS["allowed_file"], $new_item) == false) {
					$ok = false;
				} else {
					$ok = @unlink($new_item);
				}
            }
        }
        closedir($handle);
        $ok = @rmdir($item);
    }
    return $ok;
}
function get_max_file_size() {
    return '1024';
    $max = get_cfg_var("upload_max_filesize");
    if (@eregi("G$", $max)) {
        $max = substr($max, 0, -1);
        $max = round($max * 1073741824);
    } elseif (@eregi("M$", $max)) {
        $max = substr($max, 0, -1);
        $max = round($max * 1048576);
    } elseif (@eregi("K$", $max)) {
        $max = substr($max, 0, -1);
        $max = round($max * 1024);
    }
    return $max;
}
function down_home($abs_dir) {
    $real_home = @realpath($GLOBALS["home_dir"]);
    $real_dir = @realpath($abs_dir);
    if ($real_home === false || $real_dir === false) {
        if (@eregi("\\.\\.", $abs_dir)) return false;
    } else if (strcmp($real_home, @substr($real_dir, 0, strlen($real_home)))) {
        return false;
    }
    return true;
}
function id_browser() {
    $browser = $GLOBALS['__SERVER']['HTTP_USER_AGENT'];
    if (ereg('Opera(/| )([0-9].[0-9]{1,2})', $browser)) {
        return 'OPERA';
    } else if (ereg('MSIE ([0-9].[0-9]{1,2})', $browser)) {
        return 'IE';
    } else if (ereg('OmniWeb/([0-9].[0-9]{1,2})', $browser)) {
        return 'OMNIWEB';
    } else if (ereg('(Konqueror/)(.*)', $browser)) {
        return 'KONQUEROR';
    } else if (ereg('Mozilla/([0-9].[0-9]{1,2})', $browser)) {
        return 'MOZILLA';
    } else {
        return 'OTHER';
    }
}
