function solve(n, l) {
    const STARTING_CODE = 97;

    let result = [];

    for (let i = 1; i < n; i++) {
        for (let j = 1; j < n; j++) {
            for (let k = 0; k < l; k++) {
                for (let m = 0; m < l; m++) {
                    for (let d = 1; d <= n; d++) {
                        if (d > i && d > j) {
                            const firstLetter = String.fromCharCode(k + STARTING_CODE);
                            const secondLetter = String.fromCharCode(m + STARTING_CODE);
                            result.push(`${i}${j}${firstLetter}${secondLetter}${d}`);
                        }
                    }
                }
            }
        }
    }

    console.log(result.join(' '));
}

// solve(2, 4);

