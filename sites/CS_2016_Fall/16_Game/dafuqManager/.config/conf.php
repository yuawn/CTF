<?php

// Configuration Variables

// login to use dafuqManager: (true/false)
$GLOBALS["require_login"] = true;

$GLOBALS["language"] = "en";

// the filename of the dafuqManager script: (you rarely need to change this)
$GLOBALS["script_name"] = "https://" . $GLOBALS['__SERVER']['HTTP_HOST'] . $GLOBALS['__SERVER']["PHP_SELF"];

// allow Zip, Tar, TGz -> Only (experimental) Zip-support
$GLOBALS["zip"] = true;	//function_exists("gzcompress");
$GLOBALS["tar"] = false;
$GLOBALS["tgz"] = false;

// dafuqManager version:
$GLOBALS["version"] = "0.8.7-rc3";

// Global User Variables (used when $require_login==false)

// the home directory for the filemanager: (use '/', not '\' or '\\', no trailing '/')
$GLOBALS["home_dir"] = "";

// the url corresponding with the home directory: (no trailing '/')
$GLOBALS["home_url"] = "";

// show hidden files in dafuqManager: (hide files starting with '.', as in Linux/UNIX)
$GLOBALS["show_hidden"] = true;

// filenames not allowed to access: (uses PCRE regex syntax)
$GLOBALS["no_access"] = "^\.ht";

// user permissions bitfield: (1=modify, 2=password, 4=admin, add the numbers)
$GLOBALS["permissions"] = 7;

/* NOTE:
	File ".config/.htusers.php" using PCRE Regex Syntax.
	Further information go to http://www.php.net/pcre.pattern.syntax
 */

$GLOBALS["secret_key"] = 'KHomg4WfVeJNj9q5HFcWr5kc8XzE4PyzB8brEw6pQQyzmIZuRBbwDU7UE6jYjPm3';
