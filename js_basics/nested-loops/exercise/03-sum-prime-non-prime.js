function solve(input) {
    let primeSum = 0;
    let nonPrimeSum = 0;

    while (true) {
        const command = input.shift();

        if (command == 'stop') {
            break;
        }

        const currentNum = Number(command);

        if (currentNum < 0) {
            console.log('Number is negative.');
            continue;
        }

        let isPrime = true;

        for (let num = 2; num < currentNum; num++) {
            if (currentNum % num == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            primeSum += currentNum;
        } else {
            nonPrimeSum += currentNum;
        }
    }

    console.log(`Sum of all prime numbers is: ${primeSum}`);
    console.log(`Sum of all non prime numbers is: ${nonPrimeSum}`);
}

// solve(['3', '9', '0', '7', '19', '4', 'stop']);

