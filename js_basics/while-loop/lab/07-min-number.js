function solve(input) {
    let minNum = Number.POSITIVE_INFINITY;

    while (true) {
        let command = input.shift();

        if (command === 'Stop') {
            break;
        }

        let num = Number(command);

        if (num < minNum) {
            minNum = num;
        }
    }

    console.log(minNum);
}

solve(['100', '99', '80', '70', 'Stop']);

