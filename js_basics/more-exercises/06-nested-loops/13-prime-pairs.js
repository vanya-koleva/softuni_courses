function solve(start1, start2, diff1, diff2) {
    function isPrime(num) {
        if (num < 2) return false;

        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }

        return true;
    }

    let end1 = start1 + diff1;
    let end2 = start2 + diff2;

    for (let first = start1; first <= end1; first++) {
        for (let second = start2; second <= end2; second++) {
            if (isPrime(first) && isPrime(second)) {
                console.log(`${first}${second}`);
            }
        }
    }
}

// solve(10, 20, 5, 5);

