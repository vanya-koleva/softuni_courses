function solve(input) {
    const [username, ...passwords] = input;

    passwords.forEach(function (password, index) {
        if (password === Array.from(username).reverse().join('')) {
            console.log(`User ${username} logged in.`);
        } else if (index >= 3) {
            console.log(`User ${username} blocked!`);
        } else {
            console.log('Incorrect password. Try again.');
        }
    });
}

