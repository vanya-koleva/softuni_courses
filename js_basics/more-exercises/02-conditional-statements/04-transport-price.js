function solve(distance, timeOfDay) {
    const TRAIN_FARE = 0.06;
    const BUS_FARE = 0.09;
    const TAXI_INITIAL_FEE = 0.7;
    const TAXY_DAY_RATE = 0.79;
    const TAXY_NIGHT_RATE = 0.9;

    let price = 0;

    if (distance >= 100) {
        price = distance * TRAIN_FARE;
    } else if (distance >= 20) {
        price = distance * BUS_FARE;
    } else {
        switch (timeOfDay) {
            case 'day':
                price = distance * TAXY_DAY_RATE + TAXI_INITIAL_FEE;
                break;
            case 'night':
                price = distance * TAXY_NIGHT_RATE + TAXI_INITIAL_FEE;
                break;
        }
    }

    console.log(price.toFixed(2));
}

// solve(5, 'day');

