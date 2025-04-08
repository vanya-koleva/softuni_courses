function solve(startingYield) {
    let days = 0;
    let totalSpice = 0;
    let currentYield = startingYield;

    while (currentYield >= 100) {
        totalSpice += currentYield - 26;
        currentYield -= 10;
        days++;
    }

    if (totalSpice >= 26) {
        totalSpice -= 26;
    }

    console.log(days);
    console.log(totalSpice);
}

// solve(111);

