function solve(num1, operator, num2) {
    const operations = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => (b !== 0 ? a / b : 'Error: Division by zero'),
    };

    const result = operations[operator](num1, num2);

    console.log(typeof result === 'number' ? result.toFixed(2) : result);
}

// solve(5, '+', 10);
// solve(25.5, '-', 3);

