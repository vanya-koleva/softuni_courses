function solve(input) {
    let change = Number(input) * 100;
    let numCoins = 0;

    numCoins += Math.floor(change / 200);
    change %= 200;

    numCoins += Math.floor(change / 100);
    change %= 100;

    numCoins += Math.floor(change / 50);
    change %= 50;

    numCoins += Math.floor(change / 20);
    change %= 20;

    numCoins += Math.floor(change / 10);
    change %= 10;

    numCoins += Math.floor(change / 5);
    change %= 5;

    numCoins += Math.floor(change / 2);
    change %= 2;

    numCoins += Math.floor(change / 1);
    change %= 1;

    console.log(numCoins);
}

// solve(0.56);

