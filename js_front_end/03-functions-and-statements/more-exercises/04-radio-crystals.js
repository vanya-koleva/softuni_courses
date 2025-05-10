function solve(input) {
    const [target, ...chunks] = input;

    const operations = [
        { name: 'Cut', apply: x => x / 4, condition: x => x / 4 >= target },
        { name: 'Lap', apply: x => x * 0.8, condition: x => x * 0.8 >= target },
        { name: 'Grind', apply: x => x - 20, condition: x => x - 20 >= target },
        { name: 'Etch', apply: x => x - 2, condition: x => x - 2 >= target - 1 }, // Allow X-ray use
    ];

    for (let chunk of chunks) {
        console.log(`Processing chunk ${chunk} microns`);

        for (let op of operations) {
            let count = 0;

            while (op.condition(chunk)) {
                chunk = op.apply(chunk);
                count++;
            }

            if (count > 0) {
                console.log(`${op.name} x${count}`);
                chunk = Math.floor(chunk);
                console.log('Transporting and washing');
            }
        }

        // Use X-ray if off by 1 micron
        if (chunk === target - 1) {
            chunk += 1;
            console.log('X-ray x1');
        }

        console.log(`Finished crystal ${chunk} microns`);
    }
}

