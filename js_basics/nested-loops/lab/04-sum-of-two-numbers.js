function solve(arg1, arg2, arg3) {
    const start = Number(arg1);
    const end = Number(arg2);
    const magicNum = Number(arg3);
    let counter = 0;

    for (let i = start; i <= end; i++) {
        for (let j = start; j <= end; j++) {
            counter++;

            if (i + j == magicNum) {
                console.log(`Combination N:${counter} (${i} + ${j} = ${magicNum})`);
                return;
            }
        }
    }

    console.log(`${counter} combinations - neither equals ${magicNum}`);
}

// solve(1, 10, 5);

