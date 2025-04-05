function solve(input) {
    let index = 0;
    let numOfPresentations = 0;
    let totalGradesSum = 0;
    const juryNum = Number(input[index++]);

    while (true) {
        const presentation = input[index++];

        if (presentation == 'Finish') {
            break;
        }

        let gradesSum = 0;

        for (let i = 0; i < juryNum; i++) {
            gradesSum += Number(input[index++]);
        }

        numOfPresentations++;
        totalGradesSum += gradesSum;

        let avgGrade = gradesSum / juryNum;

        console.log(`${presentation} - ${avgGrade.toFixed(2)}.`);
    }

    const avgTotal = totalGradesSum / (numOfPresentations * juryNum);

    console.log(`Student's final assessment is ${avgTotal.toFixed(2)}.`);
}

// solve(['2', 'While-Loop', '6.00', '5.50', 'For-Loop', '5.84', '5.66', 'Finish']);

