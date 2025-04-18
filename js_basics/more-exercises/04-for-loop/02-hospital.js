function solve(input) {
    const period = Number(input.shift());

    let doctors = 7;
    let treatedPatients = 0;
    let untreatedPatients = 0;

    for (let i = 1; i <= period; i++) {
        if (i % 3 === 0) {
            if (untreatedPatients > treatedPatients) {
                doctors++;
            }
        }

        let patients = Number(input.shift());

        if (patients <= doctors) {
            treatedPatients += patients;
        } else {
            treatedPatients += doctors;
            untreatedPatients += patients - doctors;
        }
    }

    console.log(`Treated patients: ${treatedPatients}.`);
    console.log(`Untreated patients: ${untreatedPatients}.`);
}

// solve(['6', '25', '25', '25', '25', '25', '2']);

