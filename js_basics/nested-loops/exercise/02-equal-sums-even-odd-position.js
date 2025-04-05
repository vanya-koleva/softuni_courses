function solve(arg1, arg2) {
    const start = Number(arg1);
    const end = Number(arg2);

    let result = '';

    for (let i = start; i <= end; i++) {
        const numAsStr = String(i);

        let oddSum = 0;
        let evenSum = 0;

        for (let j = 0; j < numAsStr.length; j++) {
            if (j % 2 == 0) {
                evenSum += Number(numAsStr[j]);
            } else {
                oddSum += Number(numAsStr[j]);
            }
        }

        if (evenSum == oddSum) {
            result += numAsStr + ' ';
        }
    }

    console.log(result);
}

// solve(100000, 100050);

