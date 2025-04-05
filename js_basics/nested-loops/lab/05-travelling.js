function solve(input) {
    let index = 0;

    while (index < input.length) {
        let destination = input[index++];

        if (destination == 'End') {
            break;
        }

        let neededMoney = input[index++];
        let savedMoney = 0;

        while (savedMoney < neededMoney) {
            savedMoney += Number(input[index++]);
        }

        console.log(`Going to ${destination}!`);
    }
}

// solve([
//     'Greece',
//     '1000',
//     '200',
//     '200',
//     '300',
//     '100',
//     '150',
//     '240',
//     'Spain',
//     '1200',
//     '300',
//     '500',
//     '193',
//     '423',
//     'End',
// ]);

