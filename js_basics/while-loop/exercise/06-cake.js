function solve(input) {
    const totalNumPieces = Number(input.shift()) * Number(input.shift());
    let piecesTaken = 0;

    while (piecesTaken < totalNumPieces) {
        let command = input.shift();

        if (command == 'STOP') {
            break;
        }

        piecesTaken += Number(command);
    }

    let difference = Math.abs(totalNumPieces - piecesTaken);

    if (piecesTaken <= totalNumPieces) {
        console.log(`${difference} pieces are left.`);
    } else {
        console.log(`No more cake left! You need ${difference} pieces more.`);
    }
}

// solve(['10', '10', '20', '20', '20', '20', '21']);
// solve(['10', '2', '2', '4', '6', 'STOP']);

