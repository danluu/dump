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
    
    function filterByAuthor($books, $author) {
        $filteredBooks = [];

        foreach ($books as $book) {
            if ($book['author'] === $author) {
                $filteredBooks[] = $book;
            }
        }

        return $filteredBooks;
    }

    ?>

    <ul>
        <?php foreach(filterByAuthor($books, 'Gayle Laakmann McDowell') as $book): ?>
            <li><?= $book['author'] . ": " . $book['title'] ?></li>
        <?php endforeach; ?> 
    </ul>
</body>
</html>