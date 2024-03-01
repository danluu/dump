<?php
require "functions.php";

$heading = 'Home';

$uri = $_SERVER['REQUEST_URI'];

if ($uri === '/') {
    require "views/index.view.php";
} elseif ($uri === '/about') {
    require "views/about.view.php";
} elseif ($uri === '/contacts') {
    require "views/contacts.view.php";
} else {
    require "views/404.view.php";
}

require "views/index.view.php";