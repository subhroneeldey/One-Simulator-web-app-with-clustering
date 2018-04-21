<?php
$dbpoint=$_GET['pointarray'];
$file='locpoint.txt';
$handle = fopen($file, 'w') or die('Cannot open file:  '.$my_file);
fwrite($handle, $dbpoint);
fclose($handle);
$numbercluster=$_GET['numbercluster'];
echo(shell_exec("py example.py $numbercluster"));
//$temp2=shell_exec("java C:\xampp\htdocs\wkt_extractor\kmeans $dbpoint $numbercluster");
//console.log("executed kmeans");
?>