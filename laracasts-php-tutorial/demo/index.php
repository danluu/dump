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
    <h1><?php 
        $name = "Dark Matter";
        $read = false;

        if ($read) {
            $message = "You have read $name.";
        } else {
            $message = "You have not read $name.";
        }
        ?>

        <h1><?php echo $message ?></h1>
</body>
</html>