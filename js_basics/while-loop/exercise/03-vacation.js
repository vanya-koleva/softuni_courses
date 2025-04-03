function solve(input) {
    const MAX_SPENDING_DAYS = 5;

    const vacationPrice = Number(input.shift());

    let savedMoney = Number(input.shift());
    let totalDays = 0;
    let spendingDays = 0;

    while (true) {
        let action = input.shift();
        let sum = Number(input.shift());

        totalDays++;

        if (action == 'save') {
            savedMoney += sum;
            spendingDays = 0;

            if (savedMoney >= vacationPrice) {
                console.log(`You saved the money for ${totalDays} days.`);
                break;
            }
        } else {
            spendingDays++;
            savedMoney -= sum;

            if (savedMoney < 0) {
                savedMoney = 0;
            }

            if (spendingDays == MAX_SPENDING_DAYS) {
                console.log(`You can't save the money.`);
                console.log(totalDays);
                break;
            }
        }
    }
}

// solve(['2000', '1000', 'spend', '1200', 'save', '2000']);

