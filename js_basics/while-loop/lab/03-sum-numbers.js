function solve(input) {
    const firstNumber = Number(input[0]);
    let sum = 0;
    let index = 1;

    while (firstNumber > sum) {
        let currentNum = Number(input[index++]);
        sum += currentNum;
    }

    console.log(sum);
}

solve(['100', '10', '20', '30', '40']);

