<?php
	// Simple Web Application Firewall
	// 
	$data = $_POST['data'];
	$data = (String)$data;
	if ($data == '1' || $data == '2' || $data == '3') {
		echo 'ok';
	}