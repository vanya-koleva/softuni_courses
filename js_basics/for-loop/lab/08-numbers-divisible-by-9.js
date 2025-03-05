function solve(n, m) {
    let sum = 0;
    let output = '';

    for (let i = n; i <= m; i++) {
        if (i % 9 === 0) {
            sum += i;
            output += i + '\n';
        }
    }

    console.log(`The sum: ${sum}`);
    console.log(output);
}

solve(100, 200);

