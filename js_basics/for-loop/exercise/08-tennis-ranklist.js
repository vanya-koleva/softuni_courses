function solve(input) {
    let numberOfTournaments = Number(input[0]);
    let startingPoints = Number(input[1]);
    let pointsWon = 0;
    let tournamentsWon = 0;

    for (let i = 2; i < numberOfTournaments + 2; i++) {
        if (input[i] === 'W') {
            pointsWon += 2000;
            tournamentsWon++;
        } else if (input[i] === 'F') {
            pointsWon += 1200;
        } else if (input[i] === 'SF') {
            pointsWon += 720;
        }
    }

    let totalPoints = startingPoints + pointsWon;
    let avgPoints = Math.floor(pointsWon / numberOfTournaments);
    let percentage = (tournamentsWon / numberOfTournaments) * 100;

    console.log(`Final points: ${totalPoints}`);
    console.log(`Average points: ${avgPoints}`);
    console.log(`${percentage.toFixed(2)}%`);
}

solve(['5', '1400', 'F', 'SF', 'W', 'W', 'SF']);

