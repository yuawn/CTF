<?php


function startsWith($haystack, $needle)
{
    $length = strlen($needle);
    return (substr($haystack, 0, $length) === $needle);
}

if (isset($_POST["username"]) and isset($_POST["password"]))
{
    $username = (string)$_POST["username"];
    $password = (string)$_POST["password"];

    $h1 = sha1($username);
    $h2 = sha1($password);

    if ($username == $password)
    {
        $msg = "Your password can not be your username.";
    }
    else if ($h1 === $h2)
    {
        $msg = "Flag1: yuawn FLAG1";
        echo $msg,"\n";

	echo var_dump(strpos($username, "Snoopy_do_not_like_cats_hahahaha") !== false ) , "\n";


	echo var_dump( strpos($password, "ddaa_is_PHD") !== false ) , "\n";

	echo var_dump( startsWith($h1, "f00d") ) , "\n";


        if (strpos($username, "Snoopy_do_not_like_cats_hahahaha") !== false and
            strpos($password, "ddaa_is_PHD") !== false and
            startsWith($h1, "f00d"))
        {
            $msg .= "</br>";
            $msg .= "Flag2: $flag2";
            echo 'YUAWN!!!!! FLAG2!!!!!!!';

        }
    }
    else
    {
        echo "Invalid password.";
    }
}
?>