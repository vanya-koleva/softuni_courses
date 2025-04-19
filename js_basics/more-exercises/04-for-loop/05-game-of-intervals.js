function solve(input) {
    function calculatePercent(part) {
        return ((part / moves) * 100).toFixed(2);
    }

    const moves = Number(input[0]);

    let from0To9 = 0;
    let from10To19 = 0;
    let from20To29 = 0;
    let from30To39 = 0;
    let from40To50 = 0;
    let invalid = 0;

    let result = 0;

    for (let i = 1; i <= moves; i++) {
        const num = Number(input[i]);

        if (num < 0 || num > 50) {
            invalid++;
            result /= 2;
        } else if (num <= 9) {
            from0To9++;
            result += num * 0.2;
        } else if (num <= 19) {
            from10To19++;
            result += num * 0.3;
        } else if (num <= 29) {
            from20To29++;
            result += num * 0.4;
        } else if (num <= 39) {
            from30To39++;
            result += 50;
        } else {
            from40To50++;
            result += 100;
        }
    }

    console.log(result.toFixed(2));
    console.log(`From 0 to 9: ${calculatePercent(from0To9)}%`);
    console.log(`From 10 to 19: ${calculatePercent(from10To19)}%`);
    console.log(`From 20 to 29: ${calculatePercent(from20To29)}%`);
    console.log(`From 30 to 39: ${calculatePercent(from30To39)}%`);
    console.log(`From 40 to 50: ${calculatePercent(from40To50)}%`);
    console.log(`Invalid numbers: ${calculatePercent(invalid)}%`);
}

// solve(['10', '43', '57', '-12', '23', '12', '0', '50', '40', '30', '20']);

