function solve(input) {
    const leaders = {};

    for (const line of input) {
        if (line.endsWith('arrives')) {
            let leader = line.replace(' arrives', '');

            if (!leaders[leader]) {
                leaders[leader] = {};
            }
        } else if (line.includes(':')) {
            let [leader, armyInfo] = line.split(': ');

            if (leaders[leader]) {
                let [armyName, armyCount] = armyInfo.split(', ');
                leaders[leader][armyName] = Number(armyCount);
            }
        } else if (line.includes('+')) {
            let [armyName, count] = line.split(' + ');
            count = Number(count);

            for (const leader in leaders) {
                if (leaders[leader][armyName] !== undefined) {
                    leaders[leader][armyName] += count;
                    break;
                }
            }
        } else if (line.endsWith('defeated')) {
            let leader = line.replace(' defeated', '');
            delete leaders[leader];
        }
    }

    function totalArmyCount(armies) {
        return Object.values(armies).reduce((a, b) => a + b, 0);
    }

    const sortedLeaders = Object.entries(leaders)
        .map(([leader, armies]) => [leader, armies, totalArmyCount(armies)])
        .sort((a, b) => b[2] - a[2]);

    for (let [leader, armies] of sortedLeaders) {
        let total = totalArmyCount(armies);
        console.log(`${leader}: ${total}`);
        Object.entries(armies)
            .sort((a, b) => b[1] - a[1])
            .forEach(([armyName, count]) => {
                console.log(`>>> ${armyName} - ${count}`);
            });
    }
}

// solve([
//     'Rick Burr arrives',
//     'Fergus: Wexamp, 30245',
//     'Rick Burr: Juard, 50000',
//     'Findlay arrives',
//     'Findlay: Britox, 34540',
//     'Wexamp + 6000',
//     'Juard + 1350',
//     'Britox + 4500',
//     'Porter arrives',
//     'Porter: Legion, 55000',
//     'Legion + 302',
//     'Rick Burr defeated',
//     'Porter: Retix, 3205',
// ]);

