function solve(n) {
    const isEven = n % 2 === 0;
    const rows = isEven ? n - 1 : n;
    const mid = Math.floor(rows / 2);

    for (let i = 0; i < rows; i++) {
        const outerDashes = Math.abs(mid - i);
        const innerDashes = n - 2 * outerDashes - 2;
        const innerPart = innerDashes < 0 ? '*' : '*' + '-'.repeat(innerDashes) + '*';

        console.log('-'.repeat(outerDashes) + innerPart + '-'.repeat(outerDashes));
    }
}


