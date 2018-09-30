<html>
<head>
  <meta charset="utf-8">
  <title>T'VAAKU | UPLOAD PAGE</title>
  <link rel="stylesheet" media="screen" href="css/style3.css">
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
$target_dir = "Uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        //echo "File is an image - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }
}
echo "<br>";
echo'<img src="'.$target_file.'">';
echo "<br>";
$dir = "Uploads/";
//echo hello;
//$var1 = "anjaly";
//$bat_file = "t1.bat ".escapeshellarg($var1);
//$output = null;
//$txt = "user id date";
$myfile = file_put_contents('new.txt', $target_file.PHP_EOL , FILE_APPEND | LOCK_EX);
//echo $bat_file;
//exec($bat_file, $output);

// Open a directory, and read its contents
if (is_dir($dir)){
  if ($dh = opendir($dir)){
    while (($file = readdir($dh)) !== false){
      //echo "filename:" . $file . "<br>";
    }
    closedir($dh);
  }
}
// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["fileToUpload"]["size"] > 5000000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
&& $imageFileType != "gif" ) {
    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
echo "<br>";
echo "<br>";
echo "<a href='http://localhost/FINAL/bat.bat'><button class='button'><span>RUN THE KNN SCRIPT<br>( FAST | LESS ACCURATE) </span></button></a>";
echo "<br>";
echo "<br>";
echo "<a href='http://localhost/FINALS/batch.bat'><button class='button'><span>RUN THE NEURAL NETWORK SCRIPT<br>(SLOW | HIGHLY ACCURATE) </span></button></a>";
//header("Location: http://localhost/test/test/backend/redirect.php"); /* Redirect browser */
//exit();
?>
</h2>
</center>
</div>
</div>
<!-- scripts -->
<script src="particles.js"></script>
<script src="js/app3.js"></script>
</body>
</html>

