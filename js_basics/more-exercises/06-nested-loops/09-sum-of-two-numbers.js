function solve(start, end, magicNum) {
    let is_found = false;
    let combinationCount = 0;

    for (let x = start; x <= end; x++) {
        for (let y = start; y <= end; y++) {
            combinationCount++;

            if (x + y === magicNum) {
                console.log(`Combination N:${combinationCount} (${x} + ${y} = ${magicNum})`);
                is_found = true;
                return;
            }
        }
    }

    if (!is_found) {
        console.log(`${combinationCount} combinations - neither equals ${magicNum}`);
    }
}

// solve(1, 10, 5);

