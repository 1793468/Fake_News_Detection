function startConfetti() {
    const canvas = document.createElement("canvas");
    document.body.appendChild(canvas);
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const confetti = confetti.create(canvas, {
        resize: true,
        useWorker: true
    });
    confetti({
        particleCount: 300,
        spread: 200
    });
}
