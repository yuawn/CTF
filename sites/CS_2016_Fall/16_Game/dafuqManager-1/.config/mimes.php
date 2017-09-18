<?php

$GLOBALS["allowed_file"] = '\.(jpg|gif|png|doc|xls|c|py|js|cpp|cc|h|rb|asp|css?|java|sh)$';

// editable files:
$GLOBALS["editable_ext"] = array(
    "\.txt$|\.php$|\.php3$|\.phtml$|\.inc$|\.sql$|\.pl$",
    "\.htm$|\.html$|\.shtml$|\.dhtml$|\.xml$",
    "\.js$|\.css$|\.cgi$|\.cpp$\.c$|\.cc$|\.cxx$|\.hpp$|\.h$",
    "\.pas$|\.p$|\.java$|\.py$|\.sh$\.tcl$|\.tk$"
);

// image files:
$GLOBALS["images_ext"] = "\.png$|\.bmp$|\.jpg$|\.jpeg$|\.gif$";

// mime types: (description,image,extension)
$GLOBALS["super_mimes"] = array(
	// dir, exe, file
    "dir" => array($GLOBALS["mimes"]["dir"], "dir.png"),
    "exe" => array($GLOBALS["mimes"]["exe"], "exe.png", "\.exe$|\.com$|\.bin$"),
    "file" => array($GLOBALS["mimes"]["file"], "file.png")
);
$GLOBALS["used_mime_types"] = array(
	// text
    "text" => array($GLOBALS["mimes"]["text"], "txt.png", "\.txt$"),
	
	// programming
//	"php"	=> array($GLOBALS["mimes"]["php"],"php.png","\.php$|\.php3$|\.phtml$|\.inc$"),
    "sql" => array($GLOBALS["mimes"]["sql"], "src.png", "\.sql$"),
    "perl" => array($GLOBALS["mimes"]["perl"], "pl.png", "\.pl$"),
    "html" => array($GLOBALS["mimes"]["html"], "html.png", "\.htm$|\.html$|\.shtml$|\.dhtml$|\.xml$"),
    "js" => array($GLOBALS["mimes"]["js"], "js.png", "\.js$"),
    "css" => array($GLOBALS["mimes"]["css"], "src.png", "\.css$"),
    "cgi" => array($GLOBALS["mimes"]["cgi"], "exe.png", "\.cgi$"),
	//"py"	=> array($GLOBALS["mimes"]["py"],"py.png","\.py$"),
	//"sh"	=> array($GLOBALS["mimes"]["sh"],"sh.png","\.sh$"),
	// C++
    "cpps" => array($GLOBALS["mimes"]["cpps"], "cpp.png", "\.cpp$|\.c$|\.cc$|\.cxx$"),
    "cpph" => array($GLOBALS["mimes"]["cpph"], "h.png", "\.hpp$|\.h$"),
	// Java
    "javas" => array($GLOBALS["mimes"]["javas"], "java.png", "\.java$"),
    "javac" => array($GLOBALS["mimes"]["javac"], "java.png", "\.class$|\.jar$"),
	// Pascal
    "pas" => array($GLOBALS["mimes"]["pas"], "src.png", "\.p$|\.pas$"),
	
	// images
    "gif" => array($GLOBALS["mimes"]["gif"], "image.png", "\.gif$"),
    "jpg" => array($GLOBALS["mimes"]["jpg"], "image.png", "\.jpg$|\.jpeg$"),
    "bmp" => array($GLOBALS["mimes"]["bmp"], "image.png", "\.bmp$"),
    "png" => array($GLOBALS["mimes"]["png"], "image.png", "\.png$"),
	
	// compressed
    "zip" => array($GLOBALS["mimes"]["zip"], "zip.png", "\.zip$"),
    "tar" => array($GLOBALS["mimes"]["tar"], "tar.png", "\.tar$"),
    "gzip" => array($GLOBALS["mimes"]["gzip"], "tgz.png", "\.tgz$|\.gz$"),
    "bzip2" => array($GLOBALS["mimes"]["bzip2"], "tgz.png", "\.bz2$"),
    "rar" => array($GLOBALS["mimes"]["rar"], "tgz.png", "\.rar$"),
	//"deb"	=> array($GLOBALS["mimes"]["deb"],"package.png","\.deb$"),
	//"rpm"	=> array($GLOBALS["mimes"]["rpm"],"package.png","\.rpm$"),
	
	// music
    "mp3" => array($GLOBALS["mimes"]["mp3"], "mp3.png", "\.mp3$"),
    "wav" => array($GLOBALS["mimes"]["wav"], "sound.png", "\.wav$"),
    "midi" => array($GLOBALS["mimes"]["midi"], "midi.png", "\.mid$"),
    "real" => array($GLOBALS["mimes"]["real"], "real.png", "\.rm$|\.ra$|\.ram$"),
	//"play"	=> array($GLOBALS["mimes"]["play"],"mp3.png","\.pls$|\.m3u$"),
	
	// movie
    "mpg" => array($GLOBALS["mimes"]["mpg"], "video.png", "\.mpg$|\.mpeg$"),
    "mov" => array($GLOBALS["mimes"]["mov"], "video.png", "\.mov$"),
    "avi" => array($GLOBALS["mimes"]["avi"], "video.png", "\.avi$"),
    "flash" => array($GLOBALS["mimes"]["flash"], "flash.png", "\.swf$"),
	
	// Micosoft / Adobe
    "word" => array($GLOBALS["mimes"]["word"], "word.png", "\.doc$"),
    "excel" => array($GLOBALS["mimes"]["excel"], "spread.png", "\.xls$"),
    "pdf" => array($GLOBALS["mimes"]["pdf"], "pdf.png", "\.pdf$")
);

