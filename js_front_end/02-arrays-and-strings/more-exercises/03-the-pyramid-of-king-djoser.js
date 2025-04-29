function solve(base, increment) {
    const OVERLAP = 4;
    const LAPIS_INTERVAL = 5;

    let stone = 0;
    let marble = 0;
    let lapisLazuli = 0;
    let gold = 0;
    let step = 0;

    let currentBase = base;

    while (currentBase > 2) {
        step++;

        const perimeter = (4 * currentBase) - OVERLAP;  // subtract overlapping corners
        const innerArea = (currentBase - 2) * (currentBase - 2);

        const stoneNeeded = innerArea * increment;
        const decorativeMaterialNeeded = perimeter * increment;

        stone += stoneNeeded;

        if (step % LAPIS_INTERVAL === 0) {
            lapisLazuli += decorativeMaterialNeeded;
        } else {
            marble += decorativeMaterialNeeded;
        }

        currentBase -= 2;
    }

    step++;
    const area = currentBase * currentBase;
    gold = area * increment;

    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapisLazuli)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor(step * increment)}`);
}

