function solve(fuelType, quantity, clubCard) {
    let pricePerLitre = 0;

    if (fuelType === 'Gasoline') {
        pricePerLitre = 2.22;

        if (clubCard === 'Yes') {
            pricePerLitre -= 0.18;
        }
    } else if (fuelType === 'Diesel') {
        pricePerLitre = 2.33;

        if (clubCard === 'Yes') {
            pricePerLitre -= 0.12;
        }
    } else {
        pricePerLitre = 0.93;

        if (clubCard === 'Yes') {
            pricePerLitre -= 0.08;
        }
    }

    let totalPrice = pricePerLitre * quantity;

    if (20 <= quantity && quantity <= 25) {
        totalPrice *= 0.92;
    } else if (quantity > 25) {
        totalPrice *= 0.9;
    }

    console.log(`${totalPrice.toFixed(2)} lv.`);
}

// solve('Gas', 30, 'Yes');

