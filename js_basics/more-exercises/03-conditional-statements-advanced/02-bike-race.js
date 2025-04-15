function solve(juniorRacers, seniorRacers, trackType) {
    const prices = {
        trail: { juniors: 5.5, seniors: 7.0 },
        'cross-country': { juniors: 8.0, seniors: 9.5 },
        downhill: { juniors: 12.25, seniors: 13.75 },
        road: { juniors: 20.0, seniors: 21.5 },
    };

    const pricePerJunior = prices[trackType].juniors;
    const pricePerSenior = prices[trackType].seniors;

    const totalRacers = juniorRacers + seniorRacers;
    const discount = trackType === 'cross-country' && totalRacers >= 50 ? 0.75 : 1;

    let totalSum = (juniorRacers * pricePerJunior + seniorRacers * pricePerSenior) * discount;
    totalSum *= 0.95;

    console.log(totalSum.toFixed(2));
}

// solve(10, 20, 'trail');

