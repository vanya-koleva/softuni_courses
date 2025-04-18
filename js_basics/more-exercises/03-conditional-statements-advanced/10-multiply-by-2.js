function solve(input) {
    while (true) {
        const num = Number(input.shift());

        if (num < 0) {
            console.log('Negative number!');
            return;
        }

        console.log(`Result: ${(num * 2).toFixed(2)}`);
    }
}

// solve(['12', '43.2144', '12.3', '543.23', '-20']);

