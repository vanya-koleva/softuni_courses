function solve(age, washerPrice, pricePerToy) {
    let savedMoney = 0;
    let receivedMoney = 10;

    for (let i = 1; i <= age; i++) {
        if (i % 2 === 0) {
            savedMoney += receivedMoney - 1;
            receivedMoney += 10;
        } else {
            savedMoney += pricePerToy;
        }
    }

    let difference = Math.abs(savedMoney - washerPrice);

    if (savedMoney >= washerPrice) {
        console.log(`Yes! ${difference.toFixed(2)}`);
    } else {
        console.log(`No! ${difference.toFixed(2)}`);
    }
}

solve(10, 170.0, 6);

