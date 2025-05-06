function solve(numbers) {
    let output = '';

    for (const number of numbers) {
        output += `${number} `;
    }

    console.log(output.trim());
}

solve([ 1, 2, 3, 4, 5 ]);
