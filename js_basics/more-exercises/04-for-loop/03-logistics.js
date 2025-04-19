function solve(input) {
    const MINIBUS_PRICE = 200;
    const TRUCK_PRICE = 175;
    const TRAIN_PRICE = 120;

    const cargosNum = Number(input[0]);

    let minibus = 0;
    let truck = 0;
    let train = 0;

    for (let i = 1; i <= cargosNum; i++) {
        const cargo = Number(input[i]);

        if (cargo <= 3) {
            minibus += cargo;
        } else if (cargo <= 11) {
            truck += cargo;
        } else {
            train += cargo;
        }
    }

    const totalTons = minibus + truck + train;
    const totalPrice = minibus * MINIBUS_PRICE + truck * TRUCK_PRICE + train * TRAIN_PRICE;
    const avgPrice = totalPrice / totalTons;

    const minibusPercent = (minibus / totalTons) * 100;
    const truckPercent = (truck / totalTons) * 100;
    const trainPercent = (train / totalTons) * 100;

    console.log(avgPrice.toFixed(2));
    console.log(`${minibusPercent.toFixed(2)}%`);
    console.log(`${truckPercent.toFixed(2)}%`);
    console.log(`${trainPercent.toFixed(2)}%`);
}

// solve(['4', '1', '5', '16', '3']);

