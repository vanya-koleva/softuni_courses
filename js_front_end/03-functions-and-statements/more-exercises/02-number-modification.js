function solve(number) {
    const MIN_AVERAGE_VALUE = 5;
    const INCREMENT = '9';

    function findAverageOfDigits(numStr) {
        let sum = numStr
            .split('')
            .reduce((acc, digit) => (acc += Number(digit)), 0);

        return sum / numStr.length;
    }

    let numAsStr = number.toString();

    while (findAverageOfDigits(numAsStr) <= MIN_AVERAGE_VALUE) {
        numAsStr += INCREMENT;
    }

    console.log(numAsStr);
}

