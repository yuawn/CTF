<?php
if (isset($_SERVER)) {
    $GLOBALS['__GET'] = & $_GET;
    $GLOBALS['__POST'] = & $_POST;
    $GLOBALS['__SERVER'] = & $_SERVER;
    $GLOBALS['__FILES'] = & $_FILES;
} elseif (isset($HTTP_SERVER_VARS)) {
    $GLOBALS['__GET'] = & $HTTP_GET_VARS;
    $GLOBALS['__POST'] = & $HTTP_POST_VARS;
    $GLOBALS['__SERVER'] = & $HTTP_SERVER_VARS;
    $GLOBALS['__FILES'] = & $HTTP_POST_FILES;
} else {
    die("<B>ERROR: Your PHP version is too old</B><BR>" . "You need at least PHP 4.0.0 to run dafuqManager; preferably PHP (8)7.0.0 or higher.");
}
if (isset($GLOBALS['__GET']["action"])) $GLOBALS["action"] = $GLOBALS['__GET']["action"];
else $GLOBALS["action"] = "list";
if ($GLOBALS["action"] == "post" && isset($GLOBALS['__POST']["do_action"])) {
    $GLOBALS["action"] = $GLOBALS['__POST']["do_action"];
}
if ($GLOBALS["action"] == "") $GLOBALS["action"] = "list";
$GLOBALS["action"] = stripslashes($GLOBALS["action"]);
if (isset($GLOBALS['__GET']["dir"])) $GLOBALS["dir"] = stripslashes($GLOBALS['__GET']["dir"]);
else $GLOBALS["dir"] = "";
if ($GLOBALS["dir"] == ".") $GLOBALS["dir"] == "";
if (isset($GLOBALS['__GET']["item"])) $GLOBALS["item"] = stripslashes($GLOBALS['__GET']["item"]);
else $GLOBALS["item"] = "";
if (isset($GLOBALS['__GET']["order"])) $GLOBALS["order"] = stripslashes($GLOBALS['__GET']["order"]);
else $GLOBALS["order"] = "name";
if ($GLOBALS["order"] == "") $GLOBALS["order"] == "name";
if (isset($GLOBALS['__GET']["srt"])) $GLOBALS["srt"] = stripslashes($GLOBALS['__GET']["srt"]);
else $GLOBALS["srt"] = "yes";
if ($GLOBALS["srt"] == "") $GLOBALS["srt"] == "yes";
if (isset($GLOBALS['__GET']["lang"])) $GLOBALS["lang"] = $GLOBALS['__GET']["lang"];
elseif (isset($GLOBALS['__POST']["lang"])) $GLOBALS["lang"] = $GLOBALS['__POST']["lang"];
ob_start();
require "./.config/conf.php";
$path = "./lang/" . $GLOBALS["lang"] . ".php";
if (realpath(dirname($path)) !== realpath(dirname(__FILE__) . '/../lang/')) $GLOBALS["lang"] = "en";
if (isset($GLOBALS["lang"])) $GLOBALS["language"] = $GLOBALS["lang"];
require "./lang/" . $GLOBALS["language"] . ".php";
require "./lang/" . $GLOBALS["language"] . "_mimes.php";
require "./.config/mimes.php";
require "./core/fun_extra.php";
require "./core/header.php";
require "./core/footer.php";
require "./core/error.php";
ob_end_clean();
if ($GLOBALS["require_login"]) {
    ob_start();
    require "./core/login.php";
    ob_end_clean();
    if ($GLOBALS["action"] == "logout") {
        logout();
    } else {
        login();
    }
}
$abs_dir = get_abs_dir($GLOBALS["dir"]);
if (!@file_exists($GLOBALS["home_dir"])) {
    if ($GLOBALS["require_login"]) {
        $extra = "<A HREF=\"" . make_link("logout", NULL, NULL) . "\">" . $GLOBALS["messages"]["btnlogout"] . "</A>";
    } else $extra = NULL;
    show_error($GLOBALS["error_msg"]["home"], $extra);
}
if (!down_home($abs_dir)) show_error($GLOBALS["dir"] . " : " . $GLOBALS["error_msg"]["abovehome"]);
if (!is_dir($abs_dir)) show_error($GLOBALS["dir"] . " : " . $GLOBALS["error_msg"]["direxist"]);
