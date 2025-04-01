function solve(input) {
    let index = 0;

    while (true) {
        let word = input[index++];

        if (word === 'Stop') {
            break;
        }

        console.log(word);
    }
}

solve([
    'Nakov',
    'SoftUni',
    'Sofia',
    'Bulgaria',
    'SomeText',
    'Stop',
    'AfterStop',
    'Europe',
    'HelloWorld',
]);

