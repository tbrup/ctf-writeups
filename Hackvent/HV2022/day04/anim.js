
    const canvas = document.getElementById("canvasPiCode");
    const context = canvas.getContext("2d");
    let clientX = 0;

    canvas.addEventListener('mousemove', e => {
        clientX = e.clientX*7/1000;
    });

    let rot = [2.5132741228718345, 0.4886921905584123, -1.2566370614359172, 0, 
    	2.548180707911721, -1.9547687622336491, -0.5235987755982988, 
	1.9547687622336491, -0.3141592653589793, 0.6283185307179586, 
	-0.3141592653589793, -1.8151424220741028, 1.361356816555577, 
	0.8377580409572781, -2.443460952792061, 2.3387411976724013, 
	-0.41887902047863906, -0.3141592653589793, -0.5235987755982988,
	-0.24434609527920614, 1.8151424220741028];
    let size = canvas.width / (rot.length+2);

    context.strokeStyle = "black";
    context.lineWidth = size*5/16;
    context.shadowOffsetX = size/4;
    context.shadowOffsetY = size/4;
    context.shadowColor = "gray";
    context.shadowBlur = size/4;

    let animCount = 0;

    function anim() {
        context.clearRect(0,0,canvas.width,canvas.height);
        for (let i = 0; i < rot.length; i++) {
            context.beginPath();
            context.arc((i + 1) * size, canvas.height / 2, size * 2 / 7, rot[i]+animCount+clientX, rot[i] + 5 +animCount+clientX);
            context.stroke();
        }
        animCount+=0.001;
        requestAnimationFrame(anim);
    }
    anim();

