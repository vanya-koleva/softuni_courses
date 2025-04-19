function solve(input) {
    let index = 0;
    let maxDifference = 0;

    const pairs = Number(input[index++]);
    let value = Number(input[index++]) + Number(input[index++]);

    for (let i = 1; i < pairs; i++) {
        const currentValue = Number(input[index++]) + Number(input[index++]);

        const difference = Math.abs(value - currentValue);
        maxDifference = Math.max(maxDifference, difference);

        value = currentValue;
    }

    if (maxDifference === 0) {
        console.log(`Yes, value=${value}`);
    } else {
        console.log(`No, maxdiff=${maxDifference}`);
    }
}

// solve(['3', '1', '2', '0', '3', '4', '-1']);

