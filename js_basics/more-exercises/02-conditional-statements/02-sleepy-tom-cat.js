function solve(vacationDays) {
    const DAYS_PER_YEAR = 365;
    const PLAYTIME_NORM = 30000;
    const WORK_DAYS_PLAYTIME_PER_DAY = 63;
    const VACATION_PLAYTIME_PER_DAY = 127;

    const workingDays = DAYS_PER_YEAR - vacationDays;
    const playtime =
        vacationDays * VACATION_PLAYTIME_PER_DAY +
        workingDays * WORK_DAYS_PLAYTIME_PER_DAY;

    const difference = Math.abs(PLAYTIME_NORM - playtime);
    const hours = Math.floor(difference / 60);
    const minutes = difference % 60;

    if (playtime > PLAYTIME_NORM) {
        console.log('Tom will run away');
        console.log(`${hours} hours and ${minutes} minutes more for play`);
    } else {
        console.log('Tom sleeps well');
        console.log(`${hours} hours and ${minutes} minutes less for play`);
    }
}

// solve(20);

