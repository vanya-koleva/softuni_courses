function solve(n) {
    const STAR = '*';
    const SLASH = '/';
    const SPACE = ' ';
    const BRIDGE = '|';

    const glassSize = 2 * n;

    function printFrameRow() {
        console.log(STAR.repeat(glassSize) + SPACE.repeat(n) + STAR.repeat(glassSize));
    }

    function printMiddleRows() {
        const glasses = STAR + SLASH.repeat(glassSize - 2) + STAR;

        for (let i = 1; i <= n - 2; i++) {
            let middle = ' ';
            if (i === Math.ceil((n - 2) / 2)) {
                middle = BRIDGE.repeat(n);
            } else {
                middle = SPACE.repeat(n);
            }
            console.log(glasses + middle + glasses);
        }
    }

    printFrameRow();
    printMiddleRows();
    printFrameRow();
}

