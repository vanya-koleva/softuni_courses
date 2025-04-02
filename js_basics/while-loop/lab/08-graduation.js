function solve(input) {
    const TOTAL_CLASSES = 12;
    const PASSING_GRADE = 4;

    const name = input.shift();

    let currentClass = 1;
    let gradesSum = 0;
    let numFails = 0;

    while (input.length > 0) {
        let grade = Number(input.shift());

        if (grade < PASSING_GRADE) {
            numFails++;

            if (numFails > 1) {
                console.log(`${name} has been excluded at ${currentClass} grade`);
                break;
            }
        } else {
            gradesSum += grade;
            currentClass++;
        }

        if (currentClass > TOTAL_CLASSES) {
            let avgGrade = gradesSum / TOTAL_CLASSES;
            console.log(`${name} graduated. Average grade: ${avgGrade.toFixed(2)}`);
            break;
        }
    }
}

solve(['Gosho', '5', '5.5', '6', '5.43', '5.5', '6', '5.55', '5', '6', '6', '5.43', '5']);
solve(['Mimi', '5', '6', '5', '6', '5', '6', '6', '2', '3']);

