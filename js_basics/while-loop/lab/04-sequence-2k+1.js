function solve(input) {
    let maxNum = Number(input);
    let num = 1;

    while (num <= maxNum) {
        console.log(num);
        num = num * 2 + 1;
    }
}

solve(31);

