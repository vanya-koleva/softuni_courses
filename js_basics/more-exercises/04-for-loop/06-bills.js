function solve(input) {
    const WATER_BILL = 20;
    const INTERNET_BILL = 15;

    const months = Number(input[0]);

    let totalElectricity = 0;
    let totalOthers = 0;

    for (let i = 1; i <= months; i++) {
        const monthlyElectricity = Number(input[i]);
        totalElectricity += monthlyElectricity;

        const monthlyOthers = (monthlyElectricity + WATER_BILL + INTERNET_BILL) * 1.2;
        totalOthers += monthlyOthers;
    }

    const totalWater = WATER_BILL * months;
    const totalInternet = INTERNET_BILL * months;
    const totalSum = totalWater + totalInternet + totalElectricity + totalOthers;
    const avgBills = totalSum / months;

    console.log(`Electricity: ${totalElectricity.toFixed(2)} lv`);
    console.log(`Water: ${totalWater.toFixed(2)} lv`);
    console.log(`Internet: ${totalInternet.toFixed(2)} lv`);
    console.log(`Other: ${totalOthers.toFixed(2)} lv`);
    console.log(`Average: ${avgBills.toFixed(2)} lv`);
}

// solve(['5', '68.63', '89.25', '132.53', '93.53', '63.22']);

