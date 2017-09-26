<?php
include("flag.php");

if (isset($_GET["source"])) {
    show_source(__FILE__);
    exit();
}

$db = array(
    array("username" => "delicia", "password" => "6d386d56781b744d31328faace811444"),
    array("username" => "earnest", "password" => "907d82744bb98e956f82077a20cf92d3"),
    array("username" => "chaya", "password" => "0c914720b899f04c3522a6a467d23e07"),
    array("username" => "carlos", "password" => "4a84296507efdac241f300b4676c8448"),
    array("username" => "celine", "password" => "b74f357a8ef07a954ef3c2b780f09309"),
    array("username" => "trena", "password" => "d8a7a3e0bee98a1315f1ebeb8a6cabe5"),
    array("username" => "otis", "password" => "ca3ace395c61849f13b0a12e939ba101"),
    array("username" => "kristyn", "password" => "467bbf3d08f6d7b46a169257d2f1190a"),
    array("username" => "meaghan", "password" => "df70b80ddd44e63bc5f4eb3c4f920e77"),
    array("username" => "lacresha", "password" => "aaef40f431754fbec001172f0ce714b9"),
    array("username" => "alleen", "password" => "6d8fdad086cee23270c45a06362d03e8"),
    array("username" => "marketta", "password" => "50da5753695a6ba0514bb38d351cae81"),
    array("username" => "charlette", "password" => "3b10f46067c305ba6a10d9d3ca68e56c"),
    array("username" => "golda", "password" => "05615438bb05818cf11abb7c4bc12033"),
    array("username" => "miki", "password" => "e99a9c9124c6b4e8a7d114c95106cbb1"),
    array("username" => "adelaide", "password" => "6197a1a44aac59234fab3c7fdc872b64"),
    array("username" => "yung", "password" => "06418dc6dad833585d54e81b340c0a99"),
    array("username" => "delcie", "password" => "5f1bc54558e89ad5078ffb56bda5f86b"),
    array("username" => "alisia", "password" => "ddc21c265a7536dcf6854f5fd744b2a2"),
    array("username" => "vicki", "password" => "6bf94c6f0f5a6fac2c6859bebe2de44f"),
    array("username" => "jarrod", "password" => "6f0b8474de3252bfda8177c7f81f5bc8"),
    array("username" => "liberty", "password" => "64b73e2569bb43e6d80fffa90327e5d6"),
    array("username" => "dani", "password" => "f8aa590cb16d8746d2530f2d6b082e88"),
    array("username" => "dillon", "password" => "cb2277c9f695cd4c4d8453b531329c69"),
    array("username" => "quinton", "password" => "e322aae4dd7de048f8a5827874dcaa9b"),
    array("username" => "caridad", "password" => "edf4bcb49c1bc2e0aa720ad25978de70"),
    array("username" => "lucas", "password" => "a551c048a50263748a98a3a914da202d"),
    array("username" => "sena", "password" => "0e959146861158620914280512624073"),
    array("username" => "deja", "password" => "590aea8ba65098dccb7ee6835039f949"),
    array("username" => "fiona", "password" => "8c15dd1dcd59386d2a813eaa9ac01945"),
    array("username" => "mechelle", "password" => "ca8087d12f12a9442e1c59942173fa58"),
    array("username" => "an", "password" => "cf0d72a68a70e78f78b4b97d0fef7d89"),
    array("username" => "chadwick", "password" => "e564ee0a33eedb3cb99a8fa363ff3d39"),
    array("username" => "sandi", "password" => "8f92e127efcd049303431724661cc51a"),
    array("username" => "leola", "password" => "aa01b9fa4db785a7a4422b069a0777dd"),
    array("username" => "enid", "password" => "881592be42a22ae1011ff21bd8da57f9"),
    array("username" => "dewitt", "password" => "35646ebd5bb1bdeb05a9989cd4e2317a"),
    array("username" => "tamala", "password" => "9e2932b9be2ce2fbe6679c704fa32370"),
    array("username" => "madelaine", "password" => "ae9608b773317fb14776a1f03004ed3f"),
    array("username" => "ivan", "password" => "2bc7fce377c6a9568afa03d92c902cd7"),
    array("username" => "demetrius", "password" => "bbb3778c0359cdb6ea78a9a184396fde"),
    array("username" => "nevada", "password" => "a443c85070f9b92c6639f63bf46cf465"),
    array("username" => "lawanda", "password" => "04680fefd56ef0b2606e8df32ca7e578"),
    array("username" => "nancee", "password" => "9e1bc7ff8116dbb522a1399ef9fbca2a"),
    array("username" => "alexia", "password" => "5699f2844f7e41da9cf98aed003be6dd"),
    array("username" => "porsha", "password" => "4f38dcc1120d8824de4db6d20c892072"),
    array("username" => "edda", "password" => "fe5cc1e65c1e34046d34b6fd325729b6"),
    array("username" => "lucy", "password" => "fda2dc38e34f89e3018483fb25d7c471"),
    array("username" => "gilbert", "password" => "54ea997a290c9b00f918aa5078f8afa1"),
    array("username" => "tamica", "password" => "7a210fab1fda43d6ab88db77a43ef2f2")
);

$msg = "";
if (isset($_POST["username"]) and isset($_POST["password"]))
{
    $username = (string)$_POST["username"];
    $password = (string)$_POST["password"];

    $success = false;
    foreach ($db as $row)
    {
        if ($username == $row["username"] and md5($password) == $row["password"])
        {
            $msg = "Successful login as $username. Here's your flag: ".$flag;
            $success = true;
            break;
        }
    }
    if (!$success)
    {
        $msg = "Invalid username or password.";
    }
}
?>








int 