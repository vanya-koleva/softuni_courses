function solve(input) {
    let numberOfGroups = Number(input[0]);
    let musalaClimbers = 0;
    let montBlancClimbers = 0;
    let kilimanjaroClimbers = 0;
    let k2Climbers = 0;
    let everestClimbers = 0;

    for (let i = 0; i < numberOfGroups; i++) {
        const currentGroup = Number(input[i + 1]);

        if (currentGroup <= 5) {
            musalaClimbers += currentGroup;
        } else if (currentGroup <= 12) {
            montBlancClimbers += currentGroup;
        } else if (currentGroup <= 25) {
            kilimanjaroClimbers += currentGroup;
        } else if (currentGroup <= 40) {
            k2Climbers += currentGroup;
        } else {
            everestClimbers += currentGroup;
        }
    }

    let total =
        musalaClimbers +
        montBlancClimbers +
        kilimanjaroClimbers +
        k2Climbers +
        everestClimbers;

    console.log(`${((musalaClimbers / total) * 100).toFixed(2)}%`);
    console.log(`${((montBlancClimbers / total) * 100).toFixed(2)}%`);
    console.log(`${((kilimanjaroClimbers / total) * 100).toFixed(2)}%`);
    console.log(`${((k2Climbers / total) * 100).toFixed(2)}%`);
    console.log(`${((everestClimbers / total) * 100).toFixed(2)}%`);
}

solve(['10', '10', '5', '1', '100', '12', '26', '17', '37', '40', '78']);

