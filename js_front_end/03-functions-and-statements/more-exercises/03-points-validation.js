function solve(input) {
    const [x1, y1, x2, y2] = input;

    function isValid(xa, ya, xb, yb) {
        const distance = Math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2);
        return Number.isInteger(distance);
    }

    function printResult(xa, ya, xb, yb) {
        const valid = isValid(xa, ya, xb, yb);
        console.log(`{${xa}, ${ya}} to {${xb}, ${yb}} is ${valid ? 'valid' : 'invalid'}`);
    }

    printResult(x1, y1, 0, 0);
    printResult(x2, y2, 0, 0);
    printResult(x1, y1, x2, y2);
}

