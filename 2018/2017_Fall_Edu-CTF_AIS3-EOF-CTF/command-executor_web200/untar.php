<?php
function render() {
?>
<h1>Tar file tester</h1>

<p>Please upload a tar file to test</p>

<form enctype="multipart/form-data" action="index.php?func=untar" method="POST">
  <input type="file" name="tarfile" id="tarfile">
  <input class="btn btn-primary" type="submit" value="Upload &amp; Test">
</form>

<?php

    if(isset($_FILES['tarfile'])) {
        printf('<h2>$ tar -tvf %s</h2>', htmlentities($_FILES['tarfile']['name']));

        echo '<pre>';
        execute(sprintf('tar -tvf %s 2>&1', escapeshellarg($_FILES['tarfile']['tmp_name'])));
        echo '</pre>';
    }
}
?>
