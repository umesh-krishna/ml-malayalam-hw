<html>
<head>
  <meta charset="utf-8">
  <title>T'VAAKU | OUTPUT PAGE</title>
  <link rel="stylesheet" media="screen" href="css/style4.css">
    <style>
	#overlay{
width:27%;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.button {
  border-radius: 10px;
  background-color: #C71340;
  border: none;
  color: #ffffff;
  text-align: center;
  font-size: 15px;
  padding: 2px;
  width: 400px;
  transition: all 1.0s;
  cursor: pointer;
  margin: 5px;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 1.0s;
}

.button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -200px;
  transition: 1.0s;
}
.button:hover span:after {
  opacity: 1;
  right: 0;
}

</style>
</head>
<body>
<center>
<div id="particles-js">
<div id="overlay" style="color:white;">
<h2>
<?php
$output=shell_exec('python file.py');
echo "<center><h1><pre>";
echo "Malayalam Digital Representation is:";
print_r($output);
echo "</pre></h1></center>";
//file_put_contents("file.txt", "");
echo "<br>";
//echo "<a href='http://localhost/FINALS/heyy.php'>CREATE PDF OF TEXT</a>";
echo "<br>";
echo "<br>";
echo "<a href='http://localhost/FINALS/heyy.php'><button class='button'><span>CREATE PDF OF TEXT </span></button></a>";
//header("Location: http://localhost/test/test/backend/redirect.php"); /* Redirect browser */
//exit();
?>
</h2>
</center>
</div>
</div>
<!-- scripts -->
<script src="particles.js"></script>
<script src="js/app4.js"></script>
</body>
</html>

