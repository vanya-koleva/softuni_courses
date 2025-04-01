function solve(input) {
    let idx = 0;
    let maxNum = Number.MIN_SAFE_INTEGER;

    while (true) {
        let command = input[idx++];

        if (command === 'Stop') {
            break;
        }

        let num = Number(command);

        if (num > maxNum) {
            maxNum = num;
        }
    }

    console.log(maxNum);
}

solve(['10', '99', '80', '70', 'Stop']);

