function solve(days, foodLeft, dogFoodPerDay, catFoodPerDay, turtleFoodPerDayInGr) {
    const turtleFoodPerDay = turtleFoodPerDayInGr / 1000;

    const neededFood = days * dogFoodPerDay + days * catFoodPerDay + days * turtleFoodPerDay;
    const difference = Math.abs(neededFood - foodLeft);

    if (foodLeft >= neededFood) {
        console.log(`${Math.floor(difference)} kilos of food left.`);
    } else {
        console.log(`${Math.ceil(difference)} more kilos of food are needed.`);
    }
}

// solve(2, 10, 1, 1, 1200);

