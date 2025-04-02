function solve(input) {
    const MIN_GRADE = 4;

    const maxFails = Number(input.shift());

    let totalScore = 0;
    let numProblems = 0;
    let lastProblem = '';
    let fails = 0;

    while (fails < maxFails) {
        let problem = input.shift();

        if (problem === 'Enough') {
            const avgGrade = totalScore / numProblems;
            console.log(`Average score: ${avgGrade.toFixed(2)}`);
            console.log(`Number of problems: ${numProblems}`);
            console.log(`Last problem: ${lastProblem}`);
            break;
        }

        let grade = Number(input.shift());

        totalScore += grade;
        numProblems++;
        lastProblem = problem;

        if (grade <= MIN_GRADE) {
            fails++;
            if (fails == maxFails) {
                console.log(`You need a break, ${fails} poor grades.`);
                break;
            }
        }
    }
}

// solve(['3', 'Money', '6', 'Story', '4', 'Spring Time', '5', 'Bus', '6', 'Enough']);

