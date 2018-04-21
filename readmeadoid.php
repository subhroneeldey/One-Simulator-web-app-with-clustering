<?php
$file='medoid.txt';
$handle = fopen($file, 'r') ;
echo fread($handle,filesize("clusteringoutput.txt"));
fclose($handle);
?>