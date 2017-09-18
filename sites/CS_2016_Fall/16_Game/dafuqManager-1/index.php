<?php
ini_set('memory_limit', '16M');
ini_set('upload_max_filesize', '1k');
error_reporting(E_ALL ^ E_NOTICE ^ E_WARNING);
define('ROOT', dirname(realpath(__FILE__)));
umask(002);
require "./core/init.php";
switch ($GLOBALS["action"]) {
        // EDIT FILE
        
    case "edit":
        require "./core/fun_edit.php";
        edit_file($GLOBALS["dir"], $GLOBALS["item"]);
    break;
        // DELETE FILE(S)/DIR(S)
        
    case "delete":
        require "./core/fun_del.php";
        del_items($GLOBALS["dir"]);
    break;
        // COPY/MOVE FILE(S)/DIR(S)
        
    case "copy":
    case "move":
        require "./core/fun_copy_move.php";
        copy_move_items($GLOBALS["dir"]);
    break;
        // DOWNLOAD FILE
        
    case "download":
        ob_start(); // prevent unwanted output
        require "./core/fun_down.php";
        ob_end_clean(); // get rid of cached unwanted output
        download_item($GLOBALS["dir"], $GLOBALS["item"]);
        ob_start(false); // prevent unwanted output
        exit;
    break;
        // UPLOAD FILE(S)
        
    case "upload":
        require "./core/fun_up.php";
        upload_items($GLOBALS["dir"]);
    break;
        // CREATE DIR/FILE
        
    case "mkitem":
        require "./core/fun_mkitem.php";
        make_item($GLOBALS["dir"]);
    break;
        // CHMOD FILE/DIR
        
    case "chmod":
        require "./core/fun_chmod.php";
        chmod_item($GLOBALS["dir"], $GLOBALS["item"]);
    break;
        // SEARCH FOR FILE(S)/DIR(S)
        
    case "search":
        require "./core/fun_search.php";
        search_items($GLOBALS["dir"]);
    break;
        // CREATE ARCHIVE
        
    case "arch":
        require "./core/fun_archive.php";
        archive_items($GLOBALS["dir"]);
    break;
        // USER-ADMINISTRATION
        
    case "admin":
        require "./core/fun_admin.php";
        show_admin($GLOBALS["dir"]);
    break;
    case "debug":
        require "./core/fun_debug.php";
        do_debug($GLOBALS["dir"]);
    break;
        // DEFAULT: LIST FILES & DIRS
        
    case "list":
    default:
        require "./core/fun_list.php";
        list_dir($GLOBALS["dir"]);
} // end switch-statement
show_footer();
