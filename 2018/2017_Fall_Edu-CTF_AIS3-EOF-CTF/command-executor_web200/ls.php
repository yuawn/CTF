<?php
function render() {
    $file = '.';
    if(isset($_GET['file'])) {
        $file = (string)$_GET['file'];
    }

    echo '<h1>Dictionary Traversal</h1>';

    echo '<ul>';
    $dirs = ['.', '..', '../..', '/etc/passwd'];
    foreach($dirs as $dir) {
        printf('<li><a href="index.php?func=ls&file=%s">%1$s</a></li>', $dir);
    }
    echo '</ul>';

    printf('<h2>$ ls %s</h2>', htmlentities($file));

    echo '<pre>';
    execute(sprintf('ls -l %s', escapeshellarg($file)));
    echo '</pre>';
}
?>
