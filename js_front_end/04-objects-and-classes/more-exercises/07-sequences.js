function solve(input) {
    const unique = new Map();

    for (let str of input) {
        const arr = JSON.parse(str);
        const sorted = [...arr].sort((a, b) => a - b).toString();

        if (!unique.has(sorted)) {
            unique.set(sorted, arr);
        }
    }

    const result = Array.from(unique.values());

    result.sort((a, b) => a.length - b.length);

    for (let arr of result) {
        arr.sort((a, b) => b - a);
        console.log(`[${arr.join(', ')}]`);
    }
}

// solve(['[-3, -2, -1, 0, 1, 2, 3, 4]', '[10, 1, -17, 0, 2, 13]', '[4, -3, 3, -2, 2, -1, 1, 0]']);

