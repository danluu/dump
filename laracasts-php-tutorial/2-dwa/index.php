<?php
require "functions.php";

$heading = 'Home';

$uri = parse_url($_SERVER['REQUEST_URI'])['path'];

$routes = [
    '/' => 'controllers/index.php',
    '/about' => 'controllers/about.php',
    '/contacts' => 'controllers/contacts.php'
];

if (array_key_exists($uri, $routes)) {
    require $routes[$uri];
} else {
    require "views/404.view.php";
}