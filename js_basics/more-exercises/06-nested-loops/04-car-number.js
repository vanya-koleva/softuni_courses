function solve(start, end) {
    let result = '';

    for (let a = start; a <= end; a++) {
        for (let b = start; b <= end; b++) {
            for (let c = start; c <= end; c++) {
                for (let d = start; d <= end; d++) {
                    const isFirstEven = a % 2 === 0;
                    const isFirstOdd = a % 2 !== 0;

                    const isLastEven = d % 2 === 0;
                    const isLastOdd = d % 2 !== 0;

                    const firstRule = (isFirstEven && isLastOdd) || (isFirstOdd && isLastEven);
                    const secondRule = a > d;
                    const thirdRule = (b + c) % 2 == 0;

                    if (firstRule && secondRule && thirdRule) {
                        result += `${a}${b}${c}${d} `;
                    }
                }
            }
        }
    }

    console.log(result);
}

// solve(2, 3);

