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

 

    <ul>
        <?php foreach($filteredBooks as $book): ?>
            <li><?= $book['author'] . ": " . $book['title'] ?></li>
        <?php endforeach; ?> 
    </ul>
</body>
</html>