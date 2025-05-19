function solve(input) {
    const garages = {};

    for (const line of input) {
        let [garageNum, carInfo] = line.split(' - ');

        if (!garages[garageNum]) {
            garages[garageNum] = [];
        }

        let carDetails = carInfo
            .split(', ')
            .map(pair => {
                let [key, value] = pair.split(': ');
                return `${key} - ${value}`;
            })
            .join(', ');

        garages[garageNum].push(carDetails);
    }

    for (const [garage, cars] of Object.entries(garages)) {
        console.log(`Garage № ${garage}`);
        for (const car of cars) {
            console.log(`--- ${car}`);
        }
    }
}

// solve([
//     '1 - color: blue, fuel type: diesel',
//     '1 - color: red, manufacture: Audi',
//     '2 - fuel type: petrol',
//     '4 - color: dark blue, fuel type: diesel, manufacture: Fiat',
// ]);

