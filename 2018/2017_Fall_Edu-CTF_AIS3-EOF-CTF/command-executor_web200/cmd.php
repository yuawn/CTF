<?php
function render() {
    $cmd = '';
    if(isset($_GET['cmd'])) {
        $cmd = (string)$_GET['cmd'];
    }
?>
<h1>Command Execution</h1>
<?php
    echo '<ul>';
    $cmds = ['ls', 'env'];
    foreach($cmds as $c) {
        printf('<li><a href="index.php?func=cmd&cmd=%s">%1$s</a></li>', $c);
    }
    echo '</ul>';
?>

<form action="index.php" method="GET">
  <input type="hidden" name="func" value="cmd">
  <div class="input-group">
    <input class="form-control" type="text" name="cmd" id="cmd">
    <div class="input-group-append">
      <input class="btn btn-primary" type="submit" value="Execute">
    </div>
  </div>
</form>
<script>cmd.focus();</script>
<?php

    if(strlen($cmd) > 0) {
        printf('<h2>$ %s</h2>', htmlentities($cmd));

        echo '<pre>';
        switch ($cmd) {
        case 'env':
        case 'ls':
        case 'ls -l':
        case 'ls -al':
            execute($cmd);
            break;
        case 'cat flag':
            echo '<img src="cat-flag.png" alt="cat flag">';
            break;
        default:
            printf('%s: command not found', htmlentities($cmd));
        }
        echo '</pre>';
    }
}
?>
