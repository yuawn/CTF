<?php
if (! $FROM_INCLUDE)
    exit('not allow direct access');

function RandomString()
{
    $characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    $randstring = "";
    for ($i = 0; $i < 9; $i++) {
        $randstring .= $characters[rand(0, strlen($characters)-1)];
    }
    return $randstring;
}

$target_dir = "images";
$uploadOk = false;
if(isset($_FILES["fileToUpload"]))
{
    $filename = basename($_FILES['fileToUpload']['name']);
    $imageFileType = pathinfo($filename, PATHINFO_EXTENSION);
    if($imageFileType == "jpg")
    {
        $uploadOk = 1;
    }
    else
    {
        echo "<center><p>Sorry,we only accept jpg file</p></center>";
        $uploadOk = 0;
    }

    $fsize = $_FILES['fileToUpload']['size'];
    if(!($fsize >= 0 && $fsize <= 200000))
    {
        $uploadOk = 0;
        echo "<center><p>Sorry, the size too large.</p></center>";
    }
}

if($uploadOk)
{
    $ip = $_SERVER["REMOTE_ADDR"];

    $dir = "$target_dir/$ip";
    if(!is_dir($dir))
        mkdir($dir);

    $newid = RandomString();
    $newpath = "$dir/$newid.jpg";
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $newpath))
    {
        header("Location: $newpath");
        exit();
    }
    else
    {
        echo "<center><p>Something bad happend, please contact the AIS3 admin to solve this</p></center>";
    }
}
?>

<!-- Page Content -->
<div class="container">
    <!-- Marketing Icons Section -->
    <div class="row">
        <form method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label class="control-label">Select a good Snoopy picture (JPG only)</label>
                <input id="input-1" name="fileToUpload" type="file" class="file">
            </div>
        </form>
    </div>
    <script>
    // initialize with defaults
    $("#input-1").fileinput();

    // with plugin options
    $("#input-1").fileinput({'showUpload':false, 'previewFileType':'any'});
    </script>
</div>
