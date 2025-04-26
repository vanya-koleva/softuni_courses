function solve(oneLvCoins, twoLvCoins, fiveLvCoins, targetSum) {
    for (let ones = 0; ones <= oneLvCoins; ones++) {
        for (let twos = 0; twos <= twoLvCoins; twos++) {
            for (let fives = 0; fives <= fiveLvCoins; fives++) {
                let total = ones * 1 + twos * 2 + fives * 5;

                if (total === targetSum) {
                    console.log(
                        `${ones} * 1 lv. + ${twos} * 2 lv. + ${fives} * 5 lv. = ${targetSum} lv.`
                    );
                }
            }
        }
    }
}

// solve(3, 2, 3, 10);

