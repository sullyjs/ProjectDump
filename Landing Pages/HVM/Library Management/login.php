<!DOCTYPE html>
 
<?php
	if(isset($_POST['submit'])) {
		$user = $_POST['username'];
		$pass = $_POST['password'];
		if($user == 'admin' && $pass == 'admin'){
			echo('logging in.');
			sleep ( int 5 ) : int;
		} echo ('ERRROR');
	}
	 
	 
	 
 ?>
 <html>
 <head>
 
<title>Library Management</title>
<link rel="stylesheet" href="style.css">
 
 </head>
 
 <body>
	<h1>Login</h1>
	<div class="loginblock">
	<!-- <form action="actionpage.php"> -->
	 <form action="" method="post">
	  <p>USERNAME</p><input type="text" name="username" required><br>
	  <p>PASSWORD</p><input type="text" name="password" required><br><br>
	  <input type="submit" value="Submit" name="submit" class="submbtn">
	</form> 
	</div>


	

	
</body>
</html>