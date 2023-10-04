let win = 0;
let lose = 0;
let ties = 0;

document.getElementById("rock").onclick = function() {
    const humanChoice = 1;
    playRound(humanChoice);
};

document.getElementById("paper").onclick = function() {
    const humanChoice = 2;
    playRound(humanChoice);
};

document.getElementById("scissors").onclick = function() {
    const humanChoice = 3;
    playRound(humanChoice);
};

document.getElementById("reset").onclick = function() {
    win = 0;
    lose = 0;
    ties = 0;
    document.getElementById("win").innerHTML = win;
    document.getElementById("lose").innerHTML = lose;
    document.getElementById("tie").innerHTML = ties;
};

function playRound(humanChoice) {
    const computer = Math.random();
    let choice;

    if (computer < 1/3) {
        choice = 1;
    } else if (computer < 2/3) {
        choice = 2;
    } else {
        choice = 3;
    }

    if (choice === humanChoice) {
        ties += 1;
        document.getElementById("tie").innerHTML = ties;
    } else if (
        (choice === 2 && humanChoice === 1) ||
        (choice === 3 && humanChoice === 2) ||
        (choice === 1 && humanChoice === 3)
    ) {
        win += 1;
        document.getElementById("win").innerHTML = win;
    } else {
        lose += 1;
        document.getElementById("lose").innerHTML = lose;
    }
}
