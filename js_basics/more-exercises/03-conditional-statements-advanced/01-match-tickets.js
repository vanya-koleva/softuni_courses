function solve(budget, category, numPeople) {
    let ticketPrice = 0;

    if (category == 'VIP') {
        ticketPrice = 499.99;
    } else {
        ticketPrice = 249.99;
    }

    if (numPeople <= 4) {
        budget *= 0.25;
    } else if (numPeople <= 9) {
        budget *= 0.4;
    } else if (numPeople <= 24) {
        budget *= 0.5;
    } else if (numPeople <= 49) {
        budget *= 0.6;
    } else {
        budget *= 0.75;
    }

    const totalPrice = ticketPrice * numPeople;
    const difference = Math.abs(totalPrice - budget);

    if (budget >= totalPrice) {
        console.log(`Yes! You have ${difference.toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${difference.toFixed(2)} leva.`);
    }
}

// solve(1000, 'Normal', 1);

