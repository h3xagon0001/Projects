const linesAmount = document.getElementById("lines");
const linesPerSecondAmount = document.getElementById("linesPerSecond");

let lines = 0;
let linesPerSecond = 0;

linesAmount.innerHTML = lines;

function codeClicked() {
    lines += 1;
    linesAmount.innerHTML = lines;
}
