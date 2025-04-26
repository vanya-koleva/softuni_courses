function solve(days, hours) {
    let totalSum = 0;

    for (let day = 1; day <= days; day++) {
        let dailySum = 0;
        const is_day_even = day % 2 === 0;

        for (let hour = 1; hour <= hours; hour++) {
            const is_hour_even = hour % 2 === 0;

            if (is_day_even && !is_hour_even) {
                dailySum += 2.5;
            } else if (!is_day_even && is_hour_even) {
                dailySum += 1.25;
            } else {
                dailySum += 1;
            }
        }

        totalSum += dailySum;

        console.log(`Day: ${day} - ${dailySum.toFixed(2)} leva`);
    }

    console.log(`Total: ${totalSum.toFixed(2)} leva`);
}

// solve(2, 5);

