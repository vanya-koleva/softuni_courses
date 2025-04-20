function solve(input) {
    const targetSum = Number(input.shift());

    let index = 1;

    let cardPaymentsSum = 0;
    let cardPaymentsNum = 0;

    let cashPaymentsSum = 0;
    let cashPaymentsNum = 0;

    while (true) {
        const command = input.shift();

        if (command === 'End') {
            console.log('Failed to collect required money for charity.');
            break;
        }

        const sum = Number(command);

        if (index % 2 === 0) {
            if (sum < 10) {
                console.log('Error in transaction!');
            } else {
                cardPaymentsSum += sum;
                cardPaymentsNum++;
                console.log('Product sold!');
            }
        } else {
            if (sum > 100) {
                console.log('Error in transaction!');
            } else {
                cashPaymentsSum += sum;
                cashPaymentsNum++;
                console.log('Product sold!');
            }
        }

        if (cardPaymentsSum + cashPaymentsSum >= targetSum) {
            console.log(`Average CS: ${(cashPaymentsSum / cashPaymentsNum).toFixed(2)}`);
            console.log(`Average CC: ${(cardPaymentsSum / cardPaymentsNum).toFixed(2)}`);
            break;
        }

        index++;
    }
}

// solve(['500', '120', '8', '63', '256', '78', '317']);

