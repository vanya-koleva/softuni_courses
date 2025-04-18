function solve(money, year) {
    const STARTING_YEAR = 1800;
    const EVEN_YEAR_SPENDING = 12000;

    let age = 17;

    for (let i = STARTING_YEAR; i <= year; i++) {
        age++;
        
        if (i % 2 === 0) {
            money -= EVEN_YEAR_SPENDING;
        } else {
            money -= EVEN_YEAR_SPENDING + 50 * age;
        }
    }

    if (money >= 0) {
        console.log(
            `Yes! He will live a carefree life and will have ${money.toFixed(2)} dollars left.`
        );
    } else {
        console.log(`He will need ${Math.abs(money).toFixed(2)} dollars to survive.`);
    }
}

// solve(100000.15, 1808);

