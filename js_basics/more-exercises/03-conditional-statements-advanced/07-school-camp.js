function solve(season, groupType, studentsCount, nightsCount) {
    const prices = {
        Winter: { girls: 9.6, boys: 9.6, mixed: 10.0 },
        Spring: { girls: 7.2, boys: 7.2, mixed: 9.5 },
        Summer: { girls: 15.0, boys: 15.0, mixed: 20.0 },
    };

    const sports = {
        Winter: { girls: 'Gymnastics', boys: 'Judo', mixed: 'Ski' },
        Spring: { girls: 'Athletics', boys: 'Tennis', mixed: 'Cycling' },
        Summer: { girls: 'Volleyball', boys: 'Football', mixed: 'Swimming' },
    };

    const discountBrackets = [
        { min: 50, discount: 0.5 },
        { min: 20, discount: 0.85 },
        { min: 10, discount: 0.95 },
        { min: 0, discount: 1 },
    ];

    const pricePerNight = prices[season][groupType];
    const priceWithoutDiscounts = pricePerNight * studentsCount * nightsCount;

    const { discount } = discountBrackets.find(d => studentsCount >= d.min);
    const finalPrice = priceWithoutDiscounts * discount;

    const sport = sports[season][groupType];

    console.log(`${sport} ${finalPrice.toFixed(2)} lv.`);
}

// solve('Spring', 'girls', 20, 7);

