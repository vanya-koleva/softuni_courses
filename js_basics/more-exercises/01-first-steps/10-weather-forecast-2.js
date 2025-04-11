function solve(degrees) {
    const degreeRanges = [
        { min: 26.0, max: 35.0, description: 'Hot' },
        { min: 20.1, max: 25.9, description: 'Warm' },
        { min: 15.0, max: 20.0, description: 'Mild' },
        { min: 12.0, max: 14.9, description: 'Cool' },
        { min: 5.0, max: 11.9, description: 'Cold' },
    ];

    const weather = degreeRanges.find(
        range => degrees >= range.min && degrees <= range.max
    );
    console.log(weather ? weather.description : 'unknown');
}

// solve(16.5);

