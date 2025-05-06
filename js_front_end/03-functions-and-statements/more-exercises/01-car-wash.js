function solve(input) {
    commands = {
        soap: val => val + 10,
        water: val => val * 1.2,
        'vacuum cleaner': val => val * 1.25,
        mud: val => val * 0.9,
    };

    let cleanliness = 0;

    for (let command of input) {
        cleanliness = commands[command](cleanliness);
    }

    console.log(`The car is ${cleanliness.toFixed(2)}% clean.`);
}

