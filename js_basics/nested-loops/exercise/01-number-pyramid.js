function solve(n) {
    n = Number(n);
    let num = 1;
    let isBigger = false;

    for (let rows = 1; rows <= n; rows++) {
        let line = '';

        for (let cols = 1; cols <= rows; cols++) {
            if (num > n) {
                break;
            }

            line += num + ' ';
            num++;
        }

        console.log(line);

        if (isBigger) {
            break;
        }
    }
}

// solve(7);

