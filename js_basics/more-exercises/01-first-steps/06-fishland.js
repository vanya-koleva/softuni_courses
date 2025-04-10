function solve(mackerelPrice, spratPrice, bonitoKg, scadKg, musselsKg) {
    const MUSSELS_PRICE = 7.5;

    const bonitoTotalPrice = mackerelPrice * 1.6 * bonitoKg;
    const scadTotalPrice = spratPrice * 1.8 * scadKg;
    const musselsTotalPrice = MUSSELS_PRICE * musselsKg;

    const totalSum = bonitoTotalPrice + scadTotalPrice + musselsTotalPrice;

    console.log(totalSum.toFixed(2));
}

// solve(6.9, 4.2, 1.5, 2.5, 1);

