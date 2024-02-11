<?php $books = [
    [
        'title' => 'The Pragmatic Programmer',
        'author' => 'Andrew Hunt, David Thomas',
        'extra' => 'This is a great book for any programmer'
    ],
    [
        'title' => 'Clean Code',
        'author' => 'Robert C. Martin',
        'extra' => 'Hmmmm'
    ],
    [
        'title' => 'Cracking the Coding Interview',
        'author' => 'Gayle Laakmann McDowell',
        'extra' => '$'
    ],
    [
        'title' => 'Cracking the Tech Career',
        'author' => 'Gayle Laakmann McDowell',
        'extra' => '$'
    ]        
];

$filteredBooks = array_filter($books, function($book) {
    return $book['author'] !== 'Gayle Laakmann McDowell';
});

require 'index.view.php';

?>


