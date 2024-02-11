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

    <?php $books = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]; ?>

    <ul>
        <?php foreach($books as $book): ?>
            <li><?= $book ?></li>
        <?php endforeach; ?> 
    </ul>
</body>
</html>