function solve(maxFirst, maxSecond, maxThird) {
    const primeNumbers = [2, 3, 5, 7];

    for (let i = 2; i <= maxFirst; i += 2) {
        for (let j = 2; j <= maxSecond; j++) {
            if (!primeNumbers.includes(j)) continue;
            for (let k = 2; k <= maxThird; k += 2) {
                console.log(`${i} ${j} ${k}`);
            }
        }
    }
}

// solve(3, 5, 5);

