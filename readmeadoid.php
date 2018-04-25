<?php
$file='clusteringoutput.txt';
$handle = fopen($file, 'r') ;
echo fread($handle,filesize("clusteringoutput.txt"));
fclose($handle);
$fh = fopen( 'clusteringoutput.txt', "w+" );
fclose($fh);
?>