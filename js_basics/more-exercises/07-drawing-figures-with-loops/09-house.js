function solve(n) {
    const roofRows = Math.floor((n + 1) / 2);
    const baseRows = Math.floor(n / 2);
    const isEven = n % 2 === 0;

    function printRoof() {
        let starsNum = isEven ? 2 : 1;

        for (let i = 0; i < roofRows; i++) {
            const dashesNum = (n - starsNum) / 2;

            const stars = '*'.repeat(starsNum);
            const dashes = dashesNum > 0 ? '-'.repeat(dashesNum) : '';

            starsNum += 2;

            console.log(dashes + stars + dashes);
        }
    }

    function printBase() {
        for (let i = 0; i < baseRows; i++) {
            console.log('|' + '*'.repeat(n - 2) + '|');
        }
    }

    printRoof();
    printBase();
}

