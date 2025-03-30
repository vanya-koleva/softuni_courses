function solve(input) {
    let index = 0;
    let actorName = input[index++];
    let academyPoints = Number(input[index++]);
    let evaluatorsCount = Number(input[index++]);
    
    for (let i = 0; i < evaluatorsCount; i++) {
        let evaluatorName = input[index++];
        let evaluatorPoints = Number(input[index++]);
        
        let gainedPoints = (evaluatorName.length * evaluatorPoints) / 2;
        academyPoints += gainedPoints;
        
        if (academyPoints > 1250.5) {
            console.log(`Congratulations, ${actorName} got a nominee for leading role with ${academyPoints.toFixed(1)}!`);
            return;
        }
    }
    
    let neededPoints = (1250.5 - academyPoints).toFixed(1);
    console.log(`Sorry, ${actorName} you need ${neededPoints} more!`);
}

solve(["Zahari Baharov",
    "205",
    4,
    "Johnny Depp",
    "45",
    "Will Smith",
    "29",
    "Jet Lee",
    "10",
    "Matthew Mcconaughey",
    "39"]);
