const canvas = document.getElementById('matrix-canvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const matrix = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*';
matrix = matrix.split('');

const drops = [];
for (let x = 0; x < canvas.width; x += 20) {
    drops.push({ x, y: 0, speed: Math.random() * 2 + 2, length: Math.random() * 200 + 100 });
}

function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = '#0F0'; // Matrix rain color

    for (let i = 0; i < drops.length; i++) {
        const drop = drops[i];
        ctx.fillText(matrix[Math.floor(Math.random() * matrix.length)], drop.x, drop.y);
        drop.y += drop.speed;

        if (drop.y > canvas.height) {
            drop.y = 0;
            drop.x = Math.floor(Math.random() * canvas.width);
        }
    }
}

function updateCanvasSize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

function animate() {
    updateCanvasSize();
    draw();
    requestAnimationFrame(animate);
}

animate();
