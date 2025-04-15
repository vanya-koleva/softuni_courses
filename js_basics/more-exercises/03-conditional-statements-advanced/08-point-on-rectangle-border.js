function solve(x1, y1, x2, y2, x, y) {
    const isOnLeftOrRight = (x === x1 || x === x2) && y1 <= y && y <= y2;
    const isOnTopOrBottom = (y === y1 || y === y2) && x1 <= x && x <= x2;

    const result = isOnLeftOrRight || isOnTopOrBottom ? 'Border' : 'Inside / Outside';

    console.log(result);
}

// solve(2, -3, 12, 3, 8, -1);
