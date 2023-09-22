<?php

if ($_GET["username"] == "hvm" and $_GET["password"] == "hvm"){
header('Location: mypage.php'); } else {
	sleep ( int 5 ) : int;
	echo "Wrong Login Password or username";
	header('Location: login.html'); 
	