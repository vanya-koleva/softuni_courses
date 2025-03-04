function sumDigits(numberAsStr) {
    let sum = 0;

    for (let i = 0; i < numberAsStr.length; i++) {
        sum += Number(numberAsStr[i]);
    }

    console.log(`The sum of the digits is:${sum}`);
}

// sumDigits('1234')

