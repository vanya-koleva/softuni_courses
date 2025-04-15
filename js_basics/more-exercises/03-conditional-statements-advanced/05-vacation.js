function solve(budget, season) {
    const vacations = [
        {
            max: 1000,
            accomodation: 'Camp',
            rates: {
                Summer: { location: 'Alaska', percent: 0.65 },
                Winter: { location: 'Morocco', percent: 0.45 },
            },
        },
        {
            max: 3000,
            accomodation: 'Hut',
            rates: {
                Summer: { location: 'Alaska', percent: 0.8 },
                Winter: { location: 'Morocco', percent: 0.6 },
            },
        },
        {
            max: Infinity,
            accomodation: 'Hotel',
            rates: {
                Summer: { location: 'Alaska', percent: 0.9 },
                Winter: { location: 'Morocco', percent: 0.9 },
            },
        },
    ];

    const selectedVacation = vacations.find(v => budget <= v.max);
    const { location, percent } = selectedVacation.rates[season];
    const price = budget * percent;

    console.log(`${location} - ${selectedVacation.accomodation} - ${price.toFixed(2)}`);
}

// solve(800, 'Summer');

