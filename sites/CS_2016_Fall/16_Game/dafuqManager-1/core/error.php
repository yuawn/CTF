<?php
function show_error($error, $extra = NULL) {
    show_header($GLOBALS["error_msg"]["error"]);
    echo "<pre>";
    debug_print_backtrace();
    echo "</pre>";
    echo "<CENTER><BR>" . $GLOBALS["error_msg"]["error"] . ":" . "<BR><BR>\n";
    echo $error . "\n<BR><BR><A HREF=\"javascript:window.history.back()\">";
    echo $GLOBALS["error_msg"]["back"] . "</A>";
    if ($extra != NULL) echo " - " . $extra;
    echo "<BR><BR></CENTER>\n";
    show_footer();
    exit;
}
