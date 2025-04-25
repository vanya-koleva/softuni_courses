function solve(input) {
    const BITCOIN_PRICE = 11949.16;
    const GOLD_PRICE = 67.51;

    let bitcoinsPurchased = 0;
    let dayOfFirstBuy = 0;
    let totalMoney = 0;

    input.forEach((gold, index) => {
        if ((index + 1) % 3 === 0) {
            gold *= 0.7;
        }

        totalMoney += gold * GOLD_PRICE;

        while (totalMoney >= BITCOIN_PRICE) {
            bitcoinsPurchased++;
            totalMoney -= BITCOIN_PRICE;

            if (bitcoinsPurchased === 1) {
                dayOfFirstBuy = index + 1;
            }
        }
    });

    console.log(`Bought bitcoins: ${bitcoinsPurchased}`);

    if (bitcoinsPurchased > 0) {
        console.log(`Day of the first purchased bitcoin: ${dayOfFirstBuy}`);
    }

    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`);
}

// solve([100, 200, 300]);

