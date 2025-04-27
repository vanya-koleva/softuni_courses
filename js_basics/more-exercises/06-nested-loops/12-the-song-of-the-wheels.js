function solve(controlValue) {
    let count = 0;
    let password = '';
    const result = [];

    for (let a = 1; a <= 9; a++) {
        for (let b = 1; b <= 9; b++) {
            for (let c = 1; c <= 9; c++) {
                for (let d = 1; d <= 9; d++) {
                    const firstRule = a * b + c * d === controlValue;
                    const secondRule = a < b;
                    const thirdRule = c > d;

                    if (firstRule && secondRule && thirdRule) {
                        count++;
                        const combination = `${a}${b}${c}${d}`;
                        result.push(combination);

                        if (count === 4) {
                            password = combination;
                        }
                    }
                }
            }
        }
    }

    if (result.length > 0) {
        console.log(result.join(' '));
    }

    if (password.length > 0) {
        console.log(`Password: ${password}`);
    } else {
        console.log('No!');
    }
}

// solve(139);

