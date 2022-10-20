<?php
session_start();
unset($_SESSION["loggedin"]);
unset($_SESSION["user"]);
header("Location: login.php");
?>
