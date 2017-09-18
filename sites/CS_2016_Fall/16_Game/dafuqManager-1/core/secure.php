<?php

// My enchanced security mod for this f**king vulnerable app.
// You will not be able to break it!

function file_in_web($file)
{
    $file = realpath($file);
    if(strpos($file, ROOT) !== 0) return false;
    return true;
}

function sanitize($variable)
{
    if(strstr($variable, '..')) {
        return false; // prevent directory traversal attack
    }

    // this should prevent any injection attack
    $variable = str_replace('\'', '', $variable);

    // prevent null-byte truncate
    $variable = str_replace("\x00", '', $variable);

    // --cold-- code never bother me anyway~
    return $variable;
}
