function solve(n) {
    function firstAndLastLine() {
        console.log('+ ' + '- '.repeat(n - 2) + '+');
    }

    firstAndLastLine();

    for (let i = 0; i < n - 2; i++) {
        console.log('| ' + '- '.repeat(n - 2) + '|');
    }

    firstAndLastLine();
}

