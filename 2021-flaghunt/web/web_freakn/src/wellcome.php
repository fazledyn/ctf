<?php
error_reporting(0);
session_start();

if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] != true){
    header("Location: login.php");
    exit;
}


?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="author" content="0xAgun">
	<meta name="viewport" content="width=device-width,initial-scale=1">
	<meta name="description" content="cat flag.txt">
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<title>Secret challange | Login</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
</head>

<body>
	<?php require 'parts/_nav.php' ?>
	<?php 
	if ($login){
		echo '
		<div class="alert alert-success alert-dismissible fade show" role="alert">
			<strong>Success!</strong> Login Successfull.
			<button type="button" class="close" data-dismiss="alert" aria-label="Close">
				<span aria-hidden="true">&times;</span>
			</button>
		</div>';
	}

	?>
	<section class="h-100">
		<div class="container h-100">
			<div class="row justify-content-sm-center h-100">
				<div class="col-xxl-4 col-xl-5 col-lg-5 col-md-7 col-sm-9">
					<div class="text-center my-5">
						<img src="https://icons.getbootstrap.com/assets/icons/terminal-dash.svg" alt="logo" width="100">
					</div>
					<div class="card shadow-lg">
						<div class="card-body p-5">
							<h1 class="fs-4 card-title fw-bold mb-4 text-center">Wellcome <?php echo $_SESSION['user'] ?></h1>
							<form method="POST" action="/wellcome.php" class="needs-validation" id="fmdata">
								<div class="mb-3">
									<label class="mb-2 text-muted" for="email">Your Qoutes Title</label>
									<input id="text" type="text" class="form-control" name="try" value="" required autofocus>
                                </div>
                                <div class="mb-3">
									<label class="mb-2 text-muted" for="email">Description</label>
									<input id="text" type="text" class="form-control" name="des" value="" required autofocus>
                                </div>
								<div class="d-flex align-items-center">
									<button type="submit" class="btn btn-primary ms-auto" id="sbutton">
										Submit
									</button>
								</div>
							</form>
                            <div class="text-center">
                                <?php include 'parts/_qouts.php' ?>
                                
                            
                            </div>
						</div>
						</div>
					</div>
					<div class="text-center mt-5 text-muted">
						Copyright &copy; 2017-2021 &mdash; Hitsuka Corp 
					</div>
				</div>
			</div>
		</div>
	</section>
</body>
	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</html>
