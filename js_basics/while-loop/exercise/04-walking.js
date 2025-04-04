function solve(input) {
    const GOAL = 10000;

    let totalSteps = 0;

    while (totalSteps < GOAL) {
        let command = input.shift();

        if (command == 'Going home') {
            totalSteps += Number(input.shift());
            break;
        }

        totalSteps += Number(command);
    }

    const difference = Math.abs(totalSteps - GOAL);

    if (totalSteps >= GOAL) {
        console.log('Goal reached! Good job!');
        console.log(`${difference} steps over the goal!`);
    } else {
        console.log(`${difference} more steps to reach goal.`);
    }
}

// solve(['1000', '1500', '2000', '6500']);
// solve(['1500', '300', '2500', '3000', 'Going home', '200']);
