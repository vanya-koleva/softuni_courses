function solve(start, end, skip) {
    const startCode = start.charCodeAt(0);
    const endCode = end.charCodeAt(0);

    let count = 0;
    let result = '';

    for (let i = startCode; i <= endCode; i++) {
        for (let j = startCode; j <= endCode; j++) {
            for (let k = startCode; k <= endCode; k++) {
                const a = String.fromCharCode(i);
                const b = String.fromCharCode(j);
                const c = String.fromCharCode(k);

                if (a !== skip && b !== skip && c !== skip) {
                    result += a + b + c + ' ';
                    count++;
                }
            }
        }
    }

    console.log(result + count);
}

// solve('a', 'c', 'b');

