<!DOCTYPE html>
<html>
<head>
    <title>Python Tap Game</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- PyScript -->
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>

    <style>
        body {
            margin: 0;
            background: #f4f4f4;
            overflow: hidden;
            font-family: Arial, sans-serif;
        }
        #target {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: red;
            position: absolute;
        }
        #scoreDisplay {
            position: fixed;
            top: 15px;
            left: 15px;
            background: white;
            padding: 10px 14px;
            border-radius: 8px;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
    </style>
</head>

<body>

<div id="scoreDisplay">Score: 0</div>
<div id="target"></div>

<py-script>
from js import document
import random 

score = 0
target = document.getElementById("target")
display = document.getElementById("scoreDisplay")

def move_target():
    w = document.body.clientWidth - 80
    h = document.body.clientHeight - 80
    x = random.randint(0, w)
    y = random.randint(0, h)
    target.style.left = f"{x}px"
    target.style.top = f"{y}px"

def on_tap(event):
    global score
    score += 1
    display.innerHTML = f"Score: {score}"
    move_target()

# Call once to start
move_target()

# Attach callback
target.addEventListener("click", on_tap)
</py-script>


</body>
</html>