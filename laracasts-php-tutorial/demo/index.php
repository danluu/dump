<!doctype html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Demo</title>
    <style>
        body{
            height: 100vh;
            margin: 0;
            display: grid;
            font-family: sans-serif;
            place-items: center;
        }
        </style>
</head>

<body>
    <h1><Recommended Books/h1>

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
    
    function filterbyAuthor($items, $key, $author) {
        $filteredItems = [];

        foreach ($items as $item) {
            if ($item[$key] === $author) {
                $filteredItems[] = $item;
            }
        }

        return $filteredItems;
    };

    $filteredBooks = filterByAuthor($books, 'author', 'Gayle Laakmann McDowell');

    ?>

    <ul>
        <?php foreach($filteredBooks as $book): ?>
            <li><?= $book['author'] . ": " . $book['title'] ?></li>
        <?php endforeach; ?> 
    </ul>
</body>
</html>