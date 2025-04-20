function solve(input) {
    let index = 0;

    let oddSum = 0;
    let oddMax = Number.NEGATIVE_INFINITY;
    let oddMin = Number.POSITIVE_INFINITY;

    let evenSum = 0;
    let evenMax = Number.NEGATIVE_INFINITY;
    let evenMin = Number.POSITIVE_INFINITY;

    const n = Number(input[index++]);

    for (let i = 1; i <= n; i++) {
        const num = Number(input[index++]);

        if (i % 2 === 0) {
            evenSum += num;

            if (num > evenMax) {
                evenMax = num;
            }

            if (num < evenMin) {
                evenMin = num;
            }
        } else {
            oddSum += num;

            if (num > oddMax) {
                oddMax = num;
            }

            if (num < oddMin) {
                oddMin = num;
            }
        }
    }

    console.log(`OddSum=${oddSum.toFixed(2)},`);
    console.log(`OddMin=${oddMin !== Number.POSITIVE_INFINITY ? oddMin.toFixed(2) : 'No'},`);
    console.log(`OddMax=${oddMax !== Number.NEGATIVE_INFINITY ? oddMax.toFixed(2) : 'No'},`);
    console.log(`EvenSum=${evenSum.toFixed(2)},`);
    console.log(`EvenMin=${evenMin !== Number.POSITIVE_INFINITY ? evenMin.toFixed(2) : 'No'},`);
    console.log(`EvenMax=${evenMax !== Number.NEGATIVE_INFINITY ? evenMax.toFixed(2) : 'No'}`);
}

// solve(['6', '2', '3', '5', '4', '2', '1']);

