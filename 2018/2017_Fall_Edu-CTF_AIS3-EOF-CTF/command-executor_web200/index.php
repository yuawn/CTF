<?php
$pages = [
    ['man', 'Man'],
    ['untar', 'Tar Tester'],
    ['cmd', 'Cmd Exec'],
    ['ls', 'List files'],
];

function fuck($msg) {
    header('Content-Type: text/plain');
    echo $msg;
    exit;
}

$black_list = [
    '\/flag', '\(\)\s*\{\s*:;\s*\};'
];

function waf($a) {
    global $black_list;
    if(is_array($a)) {
        foreach($a as $key => $val) {
            waf($key);
            waf($val);
        }
    } else {
        foreach($black_list as $b) {
            if(preg_match("/$b/", $a) === 1) {
                fuck("$b detected! exit now.");
            }
        }
    }
}

waf($_SERVER);
waf($_GET);
waf($_POST);

function execute($cmd, $shell='bash') {
    system(sprintf('%s -c %s', $shell, escapeshellarg($cmd)));
}

foreach($_SERVER as $key => $val) {
    if(substr($key, 0, 5) === 'HTTP_') {
        putenv("$key=$val");
    }
}

$page = '';

if(isset($_GET['func'])) {
    $page = $_GET['func'];
    if(strstr($page, '..') !== false) {
        $page = '';
    }
}

if($page && strlen($page) > 0) {
    try {
        include("$page.php");
    } catch (Exception $e) {
    }
}

function render_default() { ?>
<p>Welcome to use our developer assistant service. We provide servial useless features to make your developing life harder.</p>

<img src="windows-run.jpg" alt="command executor">
<?php }
?><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Command Executor</title>
    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css" media="all">
    <link rel="stylesheet" href="comic-neue/font.css" media="all">
    <style>
      nav { margin-bottom: 1rem; }
      img { max-width: 100%; }
    </style>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark d-flex">
      <a class="navbar-brand" href="index.php">Command Executor</a>

      <ul class="navbar-nav">
<?php foreach($pages as list($file, $title)): ?>
        <li class="nav-item">
          <a class="nav-link" href="index.php?func=<?=$file?>"><?=$title?></a>
        </li>
<?php endforeach; ?>
      </ul>
    </nav>

    <div class="container"><?php if(is_callable('render')) render(); else render_default(); ?></div>
  </body>
</html>
