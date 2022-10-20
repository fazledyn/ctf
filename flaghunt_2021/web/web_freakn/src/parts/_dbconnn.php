<?php
$username = "root";
$password = "redacted";
$database = "users";
$server = "mysql_db";

$conn = mysqli_connect($server, $username, $password, $database);

if (!$conn){
    die("not connected" . mysqli_connect_error());
}

?>
