function solve(fuelType, quantity) {
    const ALLOWED_FUEL_TYPES = ['diesel', 'gasoline', 'gas'];

    fuelType = fuelType.toLowerCase();

    if (!ALLOWED_FUEL_TYPES.includes(fuelType)) {
        console.log('Invalid fuel!');
        return;
    }

    if (quantity >= 25) {
        console.log(`You have enough ${fuelType}.`);
    } else {
        console.log(`Fill your tank with ${fuelType}!`);
    }
}

// solve('Diesel', 10);

