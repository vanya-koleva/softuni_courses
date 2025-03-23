function solve(input) {
    let numOfTabs = Number(input[0]);
    let salary = Number(input[1]);

    for (let i = 0; i < numOfTabs && salary > 0; i++) {
        let tab = input[i + 2];

        if (tab === 'Facebook') {
            salary -= 150;
        } else if (tab === 'Instagram') {
            salary -= 100;
        } else if (tab === 'Reddit') {
            salary -= 50;
        }
    }

    if (salary > 0) {
        console.log(Number(salary));
    } else {
        console.log('You have lost your salary.');
    }
}

