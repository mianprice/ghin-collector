<?php
    $item1='2064561,2259440,0878514';
    $tmp = exec("python grabber.py $item1");
    echo $tmp;
?>
