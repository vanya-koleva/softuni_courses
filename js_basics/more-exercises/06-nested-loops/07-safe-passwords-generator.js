function solve(first, second, maxPasswords) {
    const SEPARATOR = '|';
    const A_START = 35;
    const B_START = 64;

    let aCode = A_START;
    let bCode = B_START;

    let result = '';
    let count = 0;

    for (let x = 1; x <= first; x++) {
        for (let y = 1; y <= second; y++) {
            if (count >= maxPasswords) {
                console.log(result);
                return;
            }

            let a = String.fromCharCode(aCode);
            let b = String.fromCharCode(bCode);

            let passowrd = `${a}${b}${x}${y}${b}${a}${SEPARATOR}`;
            result += passowrd;

            count++;
            aCode++;
            bCode++;

            if (aCode > 55) {
                aCode = A_START;
            }

            if (bCode > 96) {
                bCode = B_START;
            }
        }
    }

    console.log(result);
}

// solve(2, 3, 10);

