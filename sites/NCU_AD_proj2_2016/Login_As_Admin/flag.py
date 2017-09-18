



strcmp( $_POST['keyA'], base64_encode($flag) ) == 0 && strcmp( $_POST['keyB'], md5($flag) ) == 0 && sha1($_POST['keyA']) === sha1($_POST['keyB'])
