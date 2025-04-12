function solve(grapeArea, grapePerMeter, wineNeeded, workersNumber) {
    const GRAPE_PER_LITRE = 2.5;

    const harvest = grapeArea * grapePerMeter * 0.4;
    const wineProduced = harvest / GRAPE_PER_LITRE;
    const difference = Math.abs(wineProduced - wineNeeded);

    if (wineProduced < wineNeeded) {
        console.log(
            `It will be a tough winter! More ${Math.floor(difference)} liters wine needed.`
        );
    } else {
        const winePerWorker = Math.ceil(difference / workersNumber);

        console.log(`Good harvest this year! Total wine: ${Math.floor(wineProduced)} liters.`);
        console.log(`${Math.ceil(difference)} liters left -> ${winePerWorker} liters per person.`);
    }
}

// solve(650, 2, 175, 3);

