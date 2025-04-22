function solve(input) {
    const n = Number(input[0]);

    let sum = 0;

    for (let i = 1; i <= n; i++) {
        sum += Number(input[i]);
    }

    console.log((sum / n).toFixed(2));
}

solve(['4', '3', '2', '4', '2']);

