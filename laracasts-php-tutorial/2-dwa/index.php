<?php
require "functions.php";

$uri = parse_url($_SERVER['REQUEST_URI'])['path'];

$routes = [
    '/' => 'controllers/index.php',
    '/about' => 'controllers/about.php',
    '/contacts' => 'controllers/contacts.php'
];

function abort($code = 404) {
    http_response_code($code);
    require "views/{$code}.view.php";
    die();    
}

if (array_key_exists($uri, $routes)) {
    require $routes[$uri];
} else {
    abort();
}