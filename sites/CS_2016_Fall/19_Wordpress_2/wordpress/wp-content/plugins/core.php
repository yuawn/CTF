<?php
/**
 * @package f14gPrinter
 * @version 3.1415926
 */
/*
Plugin Name: Super f14g Printer
Plugin URI: https://game2.security.ntu.st
Description: This plugin can print f14g1 for you if you know the password!
Author: Inndy Lin
Version: 3.1415926
Author URI: https://inndy.tw
*/

function print_f14g()
{
	$h = 'm'.sprintf('%s%d','d',-4+9e0);
	if($h($_GET['passw0rd']) === '5ada11fd9c69c78ea65c832dd7f9bbde') {
		if(wp_get_user_ip() === '127.0.0.1') {
			eval(mcrypt_decrypt(MCRYPT_RIJNDAEL_256, $h($_GET['passw0rd'].AUTH_KEY), base64_decode('zEFnGVANrtEUTMLVyBusu4pqpHjqhn3X+cCtepGKg89VgIi6KugA+hITeeKIpnQIQM8UZbUkRpuCe/d8Rf5HFQJSawpeHoUg5NtcGam0eeTw+1bnFPT3dcPNB8IekPBDyXTyV44s3yaYMUAXZWthWHEVDFfKSjfTpPmQkB8fp6Go/qytRtiP3LyYmofhOOOV8APh0Pv34VPjCtxcJUpqIw=='), MCRYPT_MODE_CBC, $h($_GET['passw0rd'].AUTH_SALT)));
		} else {
			die('</head><body><h1>Sorry, Only admin from localhost can get flag');
		}
	}
}

add_action('wp_head', 'print_f14g');
