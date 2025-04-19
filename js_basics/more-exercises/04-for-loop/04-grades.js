function solve(input) {
    function calculatePercent(part) {
        return ((part / studentsNum) * 100).toFixed(2);
    }

    const studentsNum = Number(input[0]);

    let totalGrades = 0;
    let failingStudents = 0;
    let passingStudents = 0;
    let goodStudents = 0;
    let topStudents = 0;

    for (let i = 1; i <= studentsNum; i++) {
        const grade = Number(input[i]);
        totalGrades += grade;

        if (grade < 3) {
            failingStudents++;
        } else if (grade < 4) {
            passingStudents++;
        } else if (grade < 5) {
            goodStudents++;
        } else {
            topStudents++;
        }
    }

    const avgGrade = totalGrades / studentsNum;
    const failPercentage = calculatePercent(failingStudents);
    const passingPercentage = calculatePercent(passingStudents);
    const goodPercentage = calculatePercent(goodStudents);
    const topPercentage = calculatePercent(topStudents);

    console.log(`Top students: ${topPercentage}%`);
    console.log(`Between 4.00 and 4.99: ${goodPercentage}%`);
    console.log(`Between 3.00 and 3.99: ${passingPercentage}%`);
    console.log(`Fail: ${failPercentage}%`);
    console.log(`Average: ${avgGrade.toFixed(2)}`);
}

// solve(['10', '3.00', '2.99', '5.68', '3.01', '4', '4', '6.00', '4.50', '2.44', '5']);

