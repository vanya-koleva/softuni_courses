function solve(input) {
    const AMOUNT_IN_BOTTLE = 750;
    const AMOUNT_PER_PLATE = 5;
    const AMOUNT_PER_POT = 15;

    let platesWashed = 0;
    let potsWashed = 0;
    let counter = 0;

    let detergent = Number(input.shift()) * AMOUNT_IN_BOTTLE;

    while (detergent >= 0) {
        const command = input.shift();

        if (command === 'End') {
            break;
        }

        const dishes = Number(command);
        counter++;

        if (counter % 3 === 0) {
            detergent -= dishes * AMOUNT_PER_POT;
            potsWashed += dishes;
        } else {
            detergent -= dishes * AMOUNT_PER_PLATE;
            platesWashed += dishes;
        }
    }

    if (detergent < 0) {
        console.log(`Not enough detergent, ${Math.abs(detergent)} ml. more necessary!`);
    } else {
        console.log('Detergent was enough!');
        console.log(`${platesWashed} dishes and ${potsWashed} pots were washed.`);
        console.log(`Leftover detergent ${detergent} ml.`);
    }
}

// solve(['2 ', '53', '65', '55', 'End']);

