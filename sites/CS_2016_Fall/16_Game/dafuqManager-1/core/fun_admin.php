<?php
function admin($admin, $dir) {
    show_header($GLOBALS["messages"]["actadmin"]);
    include "./core/js_admin.php";
    echo "<BR><HR width=\"95%\"><TABLE width=\"350\"><TR><TD colspan=\"2\" class=\"header\"><B>";
    echo $GLOBALS["messages"]["actchpwd"] . ":</B></TD></TR>\n";
    echo "<FORM name=\"chpwd\" action=\"" . make_link("admin", $dir, NULL) . "\" method=\"post\">\n";
    echo "<INPUT type=\"hidden\" name=\"action2\" value=\"chpwd\">\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscoldpass"] . ": </TD><TD align=\"right\">";
    echo "<INPUT type=\"password\" name=\"oldpwd\" size=\"25\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscnewpass"] . ": </TD><TD align=\"right\">";
    echo "<INPUT type=\"password\" name=\"newpwd1\" size=\"25\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscconfnewpass"] . ": </TD><TD align=\"right\">";
    echo "<INPUT type=\"password\" name=\"newpwd2\" size=\"25\"></TD></TR>\n";
    echo "<TR><TD colspan=\"2\" align=\"right\"><INPUT type=\"submit\" value=\"" . $GLOBALS["messages"]["btnchange"];
    echo "\" onClick=\"return check_pwd();\" class=\"button\">\n</TD></TR></FORM></TABLE>\n";
    if ($admin) {
        echo "<HR width=\"95%\"><TABLE width=\"350\"><TR><TD colspan=\"6\" class=\"header\" nowrap>";
        echo "<B>" . $GLOBALS["messages"]["actusers"] . ":</B></TD></TR>\n";
        echo "<TR><TD colspan=\"5\">" . $GLOBALS["messages"]["miscuseritems"] . "</TD></TR>\n";
        echo "<FORM name=\"userform\" action=\"" . make_link("admin", $dir, NULL) . "\" method=\"post\">\n";
        echo "<INPUT type=\"hidden\" name=\"action2\" value=\"edituser\">\n";
        $cnt = count($GLOBALS["users"]);
        for ($i = 0;$i < $cnt;++$i) {
            $user = $GLOBALS["users"][$i][0];
            if (strlen($user) > 15) $user = substr($user, 0, 12) . "...";
            $home = $GLOBALS["users"][$i][2];
            if (strlen($home) > 30) $home = substr($home, 0, 27) . "...";
            echo "<TR><TD width=\"1%\"><INPUT TYPE=\"radio\" name=\"user\" value=\"";
            echo $GLOBALS["users"][$i][0] . "\"" . (($i == 0) ? " checked" : "") . "></TD>\n";
            echo "<TD width=\"30%\">" . $user . "</TD><TD width=\"60%\">" . $home . "</TD>\n";
            echo "<TD width=\"3%\">" . ($GLOBALS["users"][$i][4] ? $GLOBALS["messages"]["miscyesno"][2] : $GLOBALS["messages"]["miscyesno"][3]) . "</TD>\n";
            echo "<TD width=\"3%\">" . $GLOBALS["users"][$i][6] . "</TD>\n";
            echo "<TD width=\"3%\">" . ($GLOBALS["users"][$i][7] ? $GLOBALS["messages"]["miscyesno"][2] : $GLOBALS["messages"]["miscyesno"][3]) . "</TD></TR>\n";
        }
        echo "<TR><TD colspan=\"6\" align=\"right\">";
        echo "<input type=\"button\" value=\"" . $GLOBALS["messages"]["btnadd"];
        echo "\" onClick=\"javascript:location='" . make_link("admin", $dir, NULL) . "&action2=adduser';\" class=\"button\">\n";
        echo "<input type=\"button\" value=\"" . $GLOBALS["messages"]["btnedit"];
        echo "\" onClick=\"javascript:Edit();\" class=\"button\">\n";
        echo "<input type=\"button\" value=\"" . $GLOBALS["messages"]["btnremove"];
        echo "\" onClick=\"javascript:Delete();\" class=\"button\">\n</TD></TR></FORM></TABLE>\n";
    }
    echo "<HR width=\"95%\"><input type=\"button\" value=\"" . $GLOBALS["messages"]["btnclose"];
    echo "\" onClick=\"javascript:location='" . make_link("list", $dir, NULL) . "';\" class=\"button\"><BR><BR>\n"; ?><script language="JavaScript1.2" type="text/javascript">
<!--
    if(document.chpwd) document.chpwd.oldpwd.focus();
// -->
</script><?php
}
function changepwd($dir) {
    $pwd = md5(stripslashes($GLOBALS['__POST']["oldpwd"]));
    if ($GLOBALS['__POST']["newpwd1"] != $GLOBALS['__POST']["newpwd2"]) show_error($GLOBALS["error_msg"]["miscnopassmatch"]);
    $data = find_user($GLOBALS['__SESSION']["s_user"], $pwd);
    if ($data == NULL) show_error($GLOBALS["error_msg"]["miscnouserpass"]);
    $data[1] = md5(stripslashes($GLOBALS['__POST']["newpwd1"]));
    if (!update_user($data[0], $data)) show_error($data[0] . ": " . $GLOBALS["error_msg"]["chpass"]);
    activate_user($data[0], NULL);
    header("location: " . make_link("list", $dir, NULL));
}
function adduser($dir) {
    if (isset($GLOBALS['__POST']["confirm"]) && $GLOBALS['__POST']["confirm"] == "true") {
        $user = stripslashes($GLOBALS['__POST']["user"]);
        if ($user == "" || $GLOBALS['__POST']["home_dir"] == "") {
            show_error($GLOBALS["error_msg"]["miscfieldmissed"]);
        }
        if ($GLOBALS['__POST']["pass1"] != $GLOBALS['__POST']["pass2"]) show_error($GLOBALS["error_msg"]["miscnopassmatch"]);
        $data = find_user($user, NULL);
        if ($data != NULL) show_error($user . ": " . $GLOBALS["error_msg"]["miscuserexist"]);
        $data = array($user, md5(stripslashes($GLOBALS['__POST']["pass1"])), stripslashes($GLOBALS['__POST']["home_dir"]), stripslashes($GLOBALS['__POST']["home_url"]), $GLOBALS['__POST']["show_hidden"], stripslashes($GLOBALS['__POST']["no_access"]), $GLOBALS['__POST']["permissions"], $GLOBALS['__POST']["active"]);
        if (!add_user($data)) show_error($user . ": " . $GLOBALS["error_msg"]["adduser"]);
        header("location: " . make_link("admin", $dir, NULL));
        return;
    }
    show_header($GLOBALS["messages"]["actadmin"] . ": " . $GLOBALS["messages"]["miscadduser"]);
    include "./core/js_admin2.php";
    echo "<FORM name=\"adduser\" action=\"" . make_link("admin", $dir, NULL) . "&action2=adduser\" method=\"post\">\n";
    echo "<INPUT type=\"hidden\" name=\"confirm\" value=\"true\"><BR><TABLE width=\"450\">\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscusername"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"text\" name=\"user\" size=\"30\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscpassword"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"password\" name=\"pass1\" size=\"30\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscconfpass"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"password\" name=\"pass2\" size=\"30\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["mischomedir"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"text\" name=\"home_dir\" size=\"30\" value=\"";
    echo $GLOBALS["home_dir"] . "\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["mischomeurl"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"text\" name=\"home_url\" size=\"30\" value=\"";
    echo $GLOBALS["home_url"] . "\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscshowhidden"] . ":</TD>";
    echo "<TD align=\"right\"><SELECT name=\"show_hidden\">\n";
    echo "<OPTION value=\"0\">" . $GLOBALS["messages"]["miscyesno"][1] . "</OPTION>";
    echo "<OPTION value=\"1\">" . $GLOBALS["messages"]["miscyesno"][0] . "</OPTION>\n";
    echo "</SELECT></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["mischidepattern"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"text\" name=\"no_access\" size=\"30\" value=\"^\\.ht\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscperms"] . ":</TD><TD align=\"right\"><SELECT name=\"permissions\">\n";
    $permvalues = array(0, 1, 2, 3, 7);
    for ($i = 0;$i < count($GLOBALS["messages"]["miscpermnames"]);++$i) {
        echo "<OPTION value=\"" . $permvalues[$i] . "\">";
        echo $GLOBALS["messages"]["miscpermnames"][$i] . "</OPTION>\n";
    }
    echo "</SELECT></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscactive"] . ":</TD>";
    echo "<TD align=\"right\"><SELECT name=\"active\">\n";
    echo "<OPTION value=\"1\">" . $GLOBALS["messages"]["miscyesno"][0] . "</OPTION>";
    echo "<OPTION value=\"0\">" . $GLOBALS["messages"]["miscyesno"][1] . "</OPTION>\n";
    echo "</SELECT></TD></TR>\n";
    echo "<TR><TD colspan=\"2\" align=\"right\"><input type=\"submit\" value=\"" . $GLOBALS["messages"]["btnadd"];
    echo "\" onClick=\"return check_pwd();\" class=\"button\">\n<input type=\"button\" value=\"";
    echo $GLOBALS["messages"]["btncancel"] . "\" onClick=\"javascript:location='";
    echo make_link("admin", $dir, NULL) . "';\" class=\"button\"></TD></TR></FORM></TABLE><BR>\n"; ?><script language="JavaScript1.2" type="text/javascript">
    <!--
    if(document.adduser) document.adduser.user.focus();
        // -->
        </script><?php
}
function edituser($dir) {
    $user = stripslashes($GLOBALS['__POST']["user"]);
    $data = find_user($user, NULL);
    if ($data == NULL) show_error($user . ": " . $GLOBALS["error_msg"]["miscnofinduser"]);
    if ($self = ($user == $GLOBALS['__SESSION']["s_user"])) $dir = "";
    if (isset($GLOBALS['__POST']["confirm"]) && $GLOBALS['__POST']["confirm"] == "true") {
        $nuser = stripslashes($GLOBALS['__POST']["nuser"]);
        if ($nuser == "" || $GLOBALS['__POST']["home_dir"] == "") {
            show_error($GLOBALS["error_msg"]["miscfieldmissed"]);
        }
        if (isset($GLOBALS['__POST']["chpass"]) && $GLOBALS['__POST']["chpass"] == "true") {
            if ($GLOBALS['__POST']["pass1"] != $GLOBALS['__POST']["pass2"]) show_error($GLOBALS["error_msg"]["miscnopassmatch"]);
            $pass = md5(stripslashes($GLOBALS['__POST']["pass1"]));
        } else $pass = $data[1];
        if ($self) $GLOBALS['__POST']["active"] = 1;
        $data = array($nuser, $pass, stripslashes($GLOBALS['__POST']["home_dir"]), stripslashes($GLOBALS['__POST']["home_url"]), $GLOBALS['__POST']["show_hidden"], stripslashes($GLOBALS['__POST']["no_access"]), $GLOBALS['__POST']["permissions"], $GLOBALS['__POST']["active"]);
        if (!update_user($user, $data)) show_error($user . ": " . $GLOBALS["error_msg"]["saveuser"]);
        if ($self) activate_user($nuser, NULL);
        header("location: " . make_link("admin", $dir, NULL));
        return;
    }
    show_header($GLOBALS["messages"]["actadmin"] . ": " . sprintf($GLOBALS["messages"]["miscedituser"], $data[0]));
    include "./core/js_admin3.php";
    echo "<FORM name=\"edituser\" action=\"" . make_link("admin", $dir, NULL) . "&action2=edituser\" method=\"post\">\n";
    echo "<INPUT type=\"hidden\" name=\"confirm\" value=\"true\"><INPUT type=\"hidden\" name=\"user\" value=\"" . $data[0] . "\">\n";
    echo "<BR><TABLE width=\"450\">\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscusername"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type\"text\" name=\"nuser\" size=\"30\" value=\"";
    echo $data[0] . "\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscconfpass"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"password\" name=\"pass1\" size=\"30\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscconfnewpass"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"password\" name=\"pass2\" size=\"30\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscchpass"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"checkbox\" name=\"chpass\" value=\"true\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["mischomedir"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"text\" name=\"home_dir\" size=\"30\" value=\"";
    echo $data[2] . "\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["mischomeurl"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"text\" name=\"home_url\" size=\"30\" value=\"";
    echo $data[3] . "\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscshowhidden"] . ":</TD>";
    echo "<TD align=\"right\"><SELECT name=\"show_hidden\">\n";
    echo "<OPTION value=\"0\">" . $GLOBALS["messages"]["miscyesno"][1] . "</OPTION>";
    echo "<OPTION value=\"1\"" . ($data[4] ? " selected " : "") . ">";
    echo $GLOBALS["messages"]["miscyesno"][0] . "</OPTION>\n";
    echo "</SELECT></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["mischidepattern"] . ":</TD>\n";
    echo "<TD align=\"right\"><INPUT type=\"text\" name=\"no_access\" size=\"30\" value=\"";
    echo $data[5] . "\"></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscperms"] . ":</TD><TD align=\"right\"><SELECT name=\"permissions\">\n";
    $permvalues = array(0, 1, 2, 3, 7);
    for ($i = 0;$i < count($GLOBALS["messages"]["miscpermnames"]);++$i) {
        echo "<OPTION value=\"" . $permvalues[$i] . "\"" . ($permvalues[$i] == $data[6] ? " selected " : "") . ">";
        echo $GLOBALS["messages"]["miscpermnames"][$i] . "</OPTION>\n";
    }
    echo "</SELECT></TD></TR>\n";
    echo "<TR><TD>" . $GLOBALS["messages"]["miscactive"] . ":</TD>";
    echo "<TD align=\"right\"><SELECT name=\"active\"" . ($self ? " DISABLED " : "") . ">\n";
    echo "<OPTION value=\"1\">" . $GLOBALS["messages"]["miscyesno"][0] . "</OPTION>";
    echo "<OPTION value=\"0\"" . ($data[7] ? "" : " selected ") . ">";
    echo $GLOBALS["messages"]["miscyesno"][1] . "</OPTION>\n";
    echo "</SELECT></TD></TR>\n";
    echo "<TR><TD colspan=\"2\" align=\"right\"><input type=\"submit\" value=\"" . $GLOBALS["messages"]["btnsave"];
    echo "\" onClick=\"return check_pwd();\" class=\"button\" class=\"button\">\n<input type=\"button\" value=\"";
    echo $GLOBALS["messages"]["btncancel"] . "\" onClick=\"javascript:location='";
    echo make_link("admin", $dir, NULL) . "';\" class=\"button\"></TD></TR></FORM></TABLE><BR>\n";
}
function removeuser($dir) {
    $user = stripslashes($GLOBALS['__POST']["user"]);
    if ($user == $GLOBALS['__SESSION']["s_user"]) show_error($GLOBALS["error_msg"]["miscselfremove"]);
    if (!remove_user($user)) show_error($user . ": " . $GLOBALS["error_msg"]["deluser"]);
    header("location: " . make_link("admin", $dir, NULL));
}
function show_admin($dir) {
    $pwd = (($GLOBALS["permissions"] & 2) == 2);
    $admin = (($GLOBALS["permissions"] & 4) == 4);
    if (!$GLOBALS["require_login"]) show_error($GLOBALS["error_msg"]["miscnofunc"]);
    if (isset($GLOBALS['__GET']["action2"])) $action2 = $GLOBALS['__GET']["action2"];
    elseif (isset($GLOBALS['__POST']["action2"])) $action2 = $GLOBALS['__POST']["action2"];
    else $action2 = "";
    switch ($action2) {
        case "chpwd":
            if (!$pwd) show_error($GLOBALS["error_msg"]["accessfunc"]);
            changepwd($dir);
            break;
        case "adduser":
            if (!$admin) show_error($GLOBALS["error_msg"]["accessfunc"]);
            adduser($dir);
            break;
        case "edituser":
            if (!$admin) show_error($GLOBALS["error_msg"]["accessfunc"]);
            edituser($dir);
            break;
        case "rmuser":
            if (!$admin) show_error($GLOBALS["error_msg"]["accessfunc"]);
            removeuser($dir);
            break;
        default:
            if (!$pwd && !$admin) show_error($GLOBALS["error_msg"]["accessfunc"]);
            admin($admin, $dir);
        }
    } ?>
