<?php
$t = file_get_contents('richelieu.txt');
$bt = base64_decode($t);
file_put_contents("ar.zip",$bt);

