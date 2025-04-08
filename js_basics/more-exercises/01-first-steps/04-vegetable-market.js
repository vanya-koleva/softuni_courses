function solve(vegetablesPrice, fruitsPrice, vegetablesKg, fruitsKg) {
    const EURO_EXCHANGE_RATE = 1.94;

    const totalIncome =
        (vegetablesPrice * vegetablesKg + fruitsPrice * fruitsKg) / EURO_EXCHANGE_RATE;

    console.log(totalIncome.toFixed(2));
}

// solve(0.194, 19.4, 10, 10);

