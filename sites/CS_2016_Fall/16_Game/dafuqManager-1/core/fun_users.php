<?php
function load_users() {
    require "./.config/.htusers.php";
}
function save_users() {
    show_error($GLOBALS["error_msg"]["accessfunc"]);
    $cnt = count($GLOBALS["users"]);
    if ($cnt > 0) sort($GLOBALS["users"]);
    $content = '<?php $GLOBALS["users"]=array(';
    for ($i = 0;$i < $cnt;++$i) {
        $content.= "\n\tarray(\"" . $GLOBALS["users"][$i][0] . '","' . $GLOBALS["users"][$i][1] . '","' . $GLOBALS["users"][$i][2] . '","' . $GLOBALS["users"][$i][3] . '",' . $GLOBALS["users"][$i][4] . ',"' . $GLOBALS["users"][$i][5] . '",' . $GLOBALS["users"][$i][6] . ',' . $GLOBALS["users"][$i][7] . '),';
    }
    $content.= "\n); ?>";
    $fp = @fopen("./.config/.htusers.php", "w");
    if ($fp === false) return false;
    fputs($fp, $content);
    fclose($fp);
    return true;
}
function &find_user($user, $pass) {
    $cnt = count($GLOBALS["users"]);
    for ($i = 0;$i < $cnt;++$i) {
        if ($user == $GLOBALS["users"][$i][0]) {
            if ($pass == NULL || ($pass == $GLOBALS["users"][$i][1] && $GLOBALS["users"][$i][7])) {
                return $GLOBALS["users"][$i];
            }
        }
    }
    return NULL;
}
function activate_user($user, $pass) {
    $data = find_user($user, $pass);
    if ($data == NULL) return false;
    $GLOBALS['__SESSION']["s_user"] = $data[0];
    $GLOBALS['__SESSION']["s_pass"] = $data[1];
    $GLOBALS["home_dir"] = $data[2];
    $GLOBALS["home_url"] = $data[3];
    $GLOBALS["show_hidden"] = $data[4];
    $GLOBALS["no_access"] = $data[5];
    $GLOBALS["permissions"] = $data[6];
    return true;
}
function update_user($user, $new_data) {
    $data = & find_user($user, NULL);
    if ($data == NULL) return false;
    $data = $new_data;
    return save_users();
}
function add_user($data) {
    if (find_user($data[0], NULL)) return false;
    $GLOBALS["users"][] = $data;
    return save_users();
}
function remove_user($user) {
    $data = & find_user($user, NULL);
    if ($data == NULL) return false;
    $data = NULL;
    $cnt = count($GLOBALS["users"]);
    for ($i = 0;$i < $cnt;++$i) {
        if ($GLOBALS["users"][$i] != NULL) $save_users[] = $GLOBALS["users"][$i];
    }
    $GLOBALS["users"] = $save_users;
    return save_users();
}
