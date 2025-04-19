function solve(input) {
    function calculatePercent(part, total) {
        return ((part / total) * 100).toFixed(2) + '%';
    }

    const capacity = Number(input[0]);
    const fans = Number(input[1]);

    const sectors = { A: 0, B: 0, V: 0, G: 0 };

    for (let i = 0; i < fans; i++) {
        const sector = input[i + 2];
        sectors[sector]++;
    }

    console.log(calculatePercent(sectors.A, fans));
    console.log(calculatePercent(sectors.B, fans));
    console.log(calculatePercent(sectors.V, fans));
    console.log(calculatePercent(sectors.G, fans));
    console.log(calculatePercent(fans, capacity));
}

// solve(['76', '10', 'A', 'V', 'V', 'V', 'G', 'B', 'A', 'V', 'B', 'B']);

