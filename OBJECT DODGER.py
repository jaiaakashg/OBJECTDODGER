#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import display, HTML

display(HTML('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Block Dodger</title>
<style>
    body {
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #000;
    }
    canvas {
        border: 1px solid #fff;
        background-color: #000;
    }
    .scoreboard {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        color: #fff;
        font-size: 24px;
    }
</style>
</head>
<body>
<div class="scoreboard" id="scoreboard">Score: 0</div>
<canvas id="gameCanvas" width="600" height="400"></canvas>
<script>
    const canvas = document.getElementById('gameCanvas');
    const context = canvas.getContext('2d');
    const scoreboard = document.getElementById('scoreboard');

    const player = { width: 20, height: 20, x: canvas.width / 2 - 10, y: canvas.height - 30, speed: 5 };
    const obstacles = [];
    let score = 0;
    let gameOver = false;

    function drawPlayer() {
        context.fillStyle = '#0f0';
        context.fillRect(player.x, player.y, player.width, player.height);
    }

    function drawObstacles() {
        context.fillStyle = '#f00';
        for (const obstacle of obstacles) {
            context.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
        }
    }

    function updateObstacles() {
        for (const obstacle of obstacles) {
            obstacle.y += obstacle.speed;
            if (obstacle.y > canvas.height) {
                obstacles.splice(obstacles.indexOf(obstacle), 1);
                score++;
                updateScoreboard();
            }
            if (isColliding(player, obstacle)) {
                gameOver = true;
            }
        }

        if (Math.random() < 0.05) {
            obstacles.push({
                x: Math.random() * (canvas.width - 20),
                y: 0,
                width: 20,
                height: 20,
                speed: 2 + Math.random() * 3
            });
        }
    }

    function isColliding(rect1, rect2) {
        return !(rect1.x > rect2.x + rect2.width || rect1.x + rect1.width < rect2.x || rect1.y > rect2.y + rect2.height || rect1.y + rect1.height < rect2.y);
    }

    function updateScoreboard() {
        scoreboard.textContent = `Score: ${score}`;
    }

    function gameLoop() {
        if (gameOver) {
            context.fillStyle = '#fff';
            context.font = '24px Arial';
            context.fillText('Game Over', canvas.width / 2 - 50, canvas.height / 2);
            return;
        }

        context.clearRect(0, 0, canvas.width, canvas.height);
        drawPlayer();
        drawObstacles();
        updateObstacles();
        requestAnimationFrame(gameLoop);
    }

    canvas.addEventListener('mousemove', function(event) {
        const rect = canvas.getBoundingClientRect();
        player.x = event.clientX - rect.left - player.width / 2;
        if (player.x < 0) player.x = 0;
        if (player.x > canvas.width - player.width) player.x = canvas.width - player.width;
    });

    updateScoreboard();
    gameLoop();
</script>
</body>
</html>
'''))

