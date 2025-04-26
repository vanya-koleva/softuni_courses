function solve(men, women, maxTables) {
    let result = '';
    let tablesUsed = 0;

    for (let m = 1; m <= men; m++) {
        for (let w = 1; w <= women; w++) {
            if (tablesUsed === maxTables) {
                console.log(result.trim());
                return;
            }

            result += `(${m} <-> ${w}) `;
            tablesUsed++;
        }
    }

    console.log(result.trim());
}

// solve(2, 2, 6);

