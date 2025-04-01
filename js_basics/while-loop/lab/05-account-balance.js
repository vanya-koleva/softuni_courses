function solve(input) {
    let balance = 0;
    let idx = 0;

    while (true) {
        let command = input[idx++];

        if (command === 'NoMoreMoney') {
            break;
        }

        let sum = Number(command);

        if (sum < 0) {
            console.log('Invalid operation!');
            break;
        }

        balance += sum;
        console.log(`Increase: ${sum.toFixed(2)}`);
    }

    console.log(`Total: ${balance.toFixed(2)}`);
}

solve(['5.51', '69.42', '100', 'NoMoreMoney']);

