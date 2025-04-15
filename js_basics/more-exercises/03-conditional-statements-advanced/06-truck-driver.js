function solve(season, distance) {
    const MONTHS_IN_SEASON = 4;
    const TAX_PERCENT = 0.9;

    const rateTable = [
        {
            max: 5000,
            rates: {
                Spring: 0.75,
                Summer: 0.9,
                Autumn: 0.75,
                Winter: 1.05,
            },
        },
        {
            max: 10000,
            rates: {
                Spring: 0.95,
                Summer: 1.1,
                Autumn: 0.95,
                Winter: 1.25,
            },
        },
        {
            max: 20000,
            rates: {
                Spring: 1.45,
                Summer: 1.45,
                Autumn: 1.45,
                Winter: 1.45,
            },
        },
    ];

    const { rates } = rateTable.find(r => distance <= r.max);
    const ratePerKm = rates[season];

    const gross = distance * ratePerKm * MONTHS_IN_SEASON;
    const net = gross * TAX_PERCENT;

    console.log(net.toFixed(2));
}

// solve('Summer', 3455);

