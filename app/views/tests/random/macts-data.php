<?php

$sm = '';
$sd = '';
$y = 2018;
$m = 6;

for($i=0; $i<12; $i++){
    $mi = $m+$i; 
    if($mi>12){
        $y++;
        $m = $m-12;
    } 
    if($mi<10) $mi = "0$mi";
    $sm .= "'$y-$mi', ";
}
echo $sm;

echo "<hr>\n";

for($i=0; $i<12; $i++){
    $di = rand(31, 49); //1050
    $sd .= "$di, ";
}
echo $sd;

?>