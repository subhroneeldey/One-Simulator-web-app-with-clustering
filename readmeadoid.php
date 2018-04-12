<?php
$file='medoid.txt';
$handle = fopen($file, 'r') ;
echo fread($handle,filesize("medoid.txt"));
fclose($handle);
?>