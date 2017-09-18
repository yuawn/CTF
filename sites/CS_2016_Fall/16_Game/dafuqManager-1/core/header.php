<?php
function show_header($title) {
    header("Expires: Mon, 26 Jul 1997 05:00:00 GMT");
    header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
    header("Cache-Control: no-cache, must-revalidate");
    header("Pragma: no-cache");
    header("Content-Type: text/html; charset=" . $GLOBALS["charset"]); ?><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="<?=$GLOBALS["charset"] ?>">
    <title>dafuqManager :: <?=$title ?></title>
    <link rel="stylesheet" href="style/style.css" media="all">
</head>
<body>
<center>
<table style="width: 100%;">
  <tbody>
    <tr>
      <td class="title"><div style="margin: .2em 2.5%;"><?php
    if ($GLOBALS["require_login"] && isset($GLOBALS['__SESSION']["s_user"])) {
        echo "[" . $GLOBALS['__SESSION']["s_user"] . "] - ";
    } ?><?=$title ?></div></td>
    </tr>
  </tbody>
</table>

<?php
}
