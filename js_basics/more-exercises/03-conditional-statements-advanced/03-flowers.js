function solve(chrysanthemumsNum, rosesNum, tulipsNum, season, isHoliday) {
    const ARRANGEMENT_PRICE = 2;

    const prices = {
        Spring: { chrysanthemum: 2.0, rose: 4.1, tulip: 2.5 },
        Summer: { chrysanthemum: 2.0, rose: 4.1, tulip: 2.5 },
        Autumn: { chrysanthemum: 3.75, rose: 4.5, tulip: 4.15 },
        Winter: { chrysanthemum: 3.75, rose: 4.5, tulip: 4.15 },
    };

    const priceRise = isHoliday === 'Y' ? 1.15 : 1;

    const price =
        (chrysanthemumsNum * prices[season].chrysanthemum +
            rosesNum * prices[season].rose +
            tulipsNum * prices[season].tulip) *
        priceRise;

    const totalFlowers = chrysanthemumsNum + rosesNum + tulipsNum;

    const tulipsDiscount = season === 'Spring' && tulipsNum > 7 ? 0.95 : 1;
    const rosesDiscount = season === 'Winter' && rosesNum >= 10 ? 0.9 : 1;
    const numDiscount = totalFlowers > 20 ? 0.8 : 1;

    const finalPrice = price * tulipsDiscount * rosesDiscount * numDiscount + ARRANGEMENT_PRICE;

    console.log(finalPrice.toFixed(2));
}

// solve(2, 4, 8, 'Spring', 'Y');

