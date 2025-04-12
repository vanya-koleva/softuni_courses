function solve(volume, p1, p2, hours) {
    const firstPipeYield = p1 * hours;
    const secodnPipeYield = p2 * hours;
    const total = firstPipeYield + secodnPipeYield;

    if (total <= volume) {
        const percentageFull = (total / volume) * 100;
        const p1Percentage = (firstPipeYield / total) * 100;
        const p2Percentage = (secodnPipeYield / total) * 100;

        console.log(
            `The pool is ${percentageFull.toFixed(
                2
            )}% full. Pipe 1: ${p1Percentage.toFixed(2)}%. Pipe 2: ${p2Percentage.toFixed(
                2
            )}%.`
        );
    } else {
        const difference = total - volume;

        console.log(
            `For ${hours.toFixed(2)} hours the pool overflows with ${difference.toFixed(
                2
            )} liters.`
        );
    }
}

// solve(1000, 100, 120, 3);

