function solve(budget, season) {
    const carClasses = [
        {
            max: 100,
            class: 'Economy class',
            rates: {
                Summer: { car: 'Cabrio', percent: 0.35 },
                Winter: { car: 'Jeep', percent: 0.65 },
            },
        },
        {
            max: 500,
            class: 'Compact class',
            rates: {
                Summer: { car: 'Cabrio', percent: 0.45 },
                Winter: { car: 'Jeep', percent: 0.8 },
            },
        },
        {
            max: Infinity,
            class: 'Luxury class',
            rates: {
                Summer: { car: 'Jeep', percent: 0.9 },
                Winter: { car: 'Jeep', percent: 0.9 },
            },
        },
    ];

    const selectedClass = carClasses.find(car => budget <= car.max);

    // const car = selectedClass.rates[season].car;
    // const percent = selectedClass.rates[season].percent;
    const { car, percent } = selectedClass.rates[season];
    const price = budget * percent;

    console.log(`${selectedClass.class}`);
    console.log(`${car} - ${price.toFixed(2)}`);
}

// solve(450, 'Summer');

