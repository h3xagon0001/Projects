var timer = 0;

function timerFunction(){
    timer = timer + 0.01;
    document.getElementById("timer").innerHTML = timer.toFixed(2);
}

setInterval(timerFunction, 10)