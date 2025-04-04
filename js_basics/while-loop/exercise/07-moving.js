function solve(input) {
    const totalSpace =
        Number(input.shift()) * Number(input.shift()) * Number(input.shift());
    let spaceTaken = 0;

    while (spaceTaken < totalSpace) {
        let command = input.shift();

        if (command == 'Done') {
            break;
        }

        spaceTaken += Number(command);
    }

    const difference = Math.abs(totalSpace - spaceTaken);

    if (spaceTaken <= totalSpace) {
        console.log(`${difference} Cubic meters left.`);
    } else {
        console.log(`No more free space! You need ${difference} Cubic meters more.`);
    }
}

// solve(['10', '10', '2', '20', '20', '20', '20', '122']);

