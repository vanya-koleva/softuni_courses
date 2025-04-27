function solve(n) {
    function printRow(row, n) {
        const spaces = ' '.repeat(n - row);
        let stars = '*';
        if (row > 1) {
            stars += ' *'.repeat(row - 1);
        }
        console.log(spaces + stars);
    }

    function upperPart() {
        for (let row = 1; row <= n; row++) {
            printRow(row, n);
        }
    }

    function lowerPart() {
        for (let row = n - 1; row >= 1; row--) {
            printRow(row, n);
        }
    }

    upperPart();
    lowerPart();
}

