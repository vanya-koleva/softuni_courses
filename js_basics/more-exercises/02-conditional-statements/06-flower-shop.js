function solve(magnoliasNum, hyacinthsNum, rosesNum, cactusesNum, giftPrice) {
    const MAGNOLIA_PRICE = 3.25;
    const HYACINTH_PRICE = 4;
    const ROSE_PRICE = 3.5;
    const CACTUS_PRICE = 8;

    const totalSum =
        MAGNOLIA_PRICE * magnoliasNum +
        HYACINTH_PRICE * hyacinthsNum +
        ROSE_PRICE * rosesNum +
        CACTUS_PRICE * cactusesNum;
    const profit = totalSum * 0.95;

    const difference = Math.abs(profit - giftPrice);

    if (profit >= giftPrice) {
        console.log(`She is left with ${Math.floor(difference)} leva.`);
    } else {
        console.log(`She will have to borrow ${Math.ceil(difference)} leva.`);
    }
}

// solve(2, 3, 5, 1, 50);

