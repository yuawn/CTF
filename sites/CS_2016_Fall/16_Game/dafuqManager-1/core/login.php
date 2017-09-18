<?php
function logout() {
    $GLOBALS['__SESSION'] = array();
    session_destroy();
    header("location: " . $GLOBALS["script_name"]);
}
require "./core/fun_users.php";
load_users();
session_start();
if (isset($_SESSION)) {
    $GLOBALS['__SESSION'] = & $_SESSION;
} elseif (isset($HTTP_SESSION_VARS)) {
    $GLOBALS['__SESSION'] = & $HTTP_SESSION_VARS;
} else {
    logout();
    exit;
}
function login() {
    if (isset($GLOBALS['__SESSION']["s_user"])) {
        if (!activate_user($GLOBALS['__SESSION']["s_user"], $GLOBALS['__SESSION']["s_pass"])) {
            logout();
        }
    } else {
        if (isset($GLOBALS['__POST']["p_pass"])) $p_pass = $GLOBALS['__POST']["p_pass"];
        else $p_pass = "";
        if (isset($GLOBALS['__POST']["p_user"])) {
            if (!activate_user(stripslashes($GLOBALS['__POST']["p_user"]), md5(stripslashes($p_pass)))) {
                logout();
            }
            return;
        } else {
            show_header($GLOBALS["messages"]["actlogin"]);
            echo "<BR><TABLE width=\"300\"><TR><TD colspan=\"2\" class=\"header\" nowrap><B>";
            echo $GLOBALS["messages"]["actloginheader"] . "</B></TD></TR>\n<FORM name=\"login\" action=\"";
            echo make_link("login", NULL, NULL) . "\" method=\"post\">\n";
            echo "<TR><TD>" . $GLOBALS["messages"]["miscusername"] . ":</TD><TD align=\"right\">";
            echo "<INPUT name=\"p_user\" type=\"text\" size=\"25\"></TD></TR>\n";
            echo "<TR><TD>" . $GLOBALS["messages"]["miscpassword"] . ":</TD><TD align=\"right\">";
            echo "<INPUT name=\"p_pass\" type=\"password\" size=\"25\"></TD></TR>\n";
            echo "<TR><TD>" . $GLOBALS["messages"]["misclang"] . ":</TD><TD align=\"right\">";
            echo "<SELECT name=\"lang\">\n";
            @include "./lang/info.php";
            echo "</SELECT></TD></TR>\n";
            echo "<TR><TD colspan=\"2\" align=\"right\"><INPUT type=\"submit\" value=\"";
            echo $GLOBALS["messages"]["btnlogin"] . "\" class=\"button\"></TD></TR>\n</FORM></TABLE><BR>guest / guest for test\n"; ?><script language="JavaScript1.2" type="text/javascript">
<!--
    if(document.login) document.login.p_user.focus();
// -->
</script><?php
            show_footer();
            exit;
        }
    }
}
