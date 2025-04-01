function solve(input) {
    const username = input[0];
    const password = input[1];
    let index = 2;

    while (true) {
        let attempt = input[index++];

        if (attempt === password) {
            console.log(`Welcome ${username}!`);
            break;
        }
    }
}

solve(['Nakov', '1234', 'Pass', '1324', '1234']);

