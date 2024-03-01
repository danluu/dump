<?php

$heading = 'Home';

function dd($value) {
    echo "<pre>";
    var_dump($value);
    echo "</pre>";
    die();
}

dd($_SERVER);
require "views/index.view.php";