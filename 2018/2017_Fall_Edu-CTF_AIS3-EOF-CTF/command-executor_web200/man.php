<?php
function render() {
    $file = 'man';
    if(isset($_GET['file'])) {
        $file = (string)$_GET['file'];
        if(preg_match('/^[\w\-]+$/', $file) === false) {
            echo '<pre>Invalid file name!</pre>';
            return;
        }
    }

    echo '<h1>Online documents</h1>';

    $cmds = [
        'bash', 'ls', 'cp', 'mv'
    ];

    echo '<ul>';
    foreach($cmds as $cmd) {
        printf('<li><a href="index.php?func=man&file=%s">%1$s</a></li>', $cmd);
    }
    echo '</ul>';

    printf('<h2>$ man %s</h2>', htmlentities($file));

    echo '<pre>';
    execute(sprintf('man %s | cat', escapeshellarg($file)));
    echo '</pre>';
}
?>
