<nav class="navbar navbar-expand-lg navbar-light bg-light shadow d-flex justify-content-center">
  <a class="navbar-brand" href="#">Secret</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse d-flex justify-content-center" id="navbarSupportedContent">
    <ul class="navbar-nav mx-auto">
      <li class="nav-item active">
        <a class="nav-link" href="wellcome.php">Home</a>
      </li>
      <?php
      if (!isset($_SESSION['loggedin'])){
        echo '<li class="nav-item">
            <a class="nav-link" href="login.php">Login</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="signup.php">Signup</a>
        </li>';
      } else{
          echo '<li class="nav-item">
          <a class="nav-link" href="logout.php">Logout</a>
        </li>';
      }
      ?>

      <li class="nav-item">
        <a class="nav-link disabled">Disabled</a>
      </li>
    </ul>

  </div>
</nav>