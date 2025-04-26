function solve(hundredsLimit, tensLimit, unitsLimit) {
    // const primes = [2, 3, 5, 7]; // prime numbers between 2 and 7;

    function isPrime(num) {
        if (num < 2) return false;

        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }

        return true;
    }

    for (let h = 2; h <= hundredsLimit; h++) {
        if (h % 2 !== 0) continue;

        for (let t = 2; t <= tensLimit; t++) {
            // if (!primes.includes(t)) continue;
            if (!isPrime(t)) continue;

            for (let u = 2; u <= unitsLimit; u++) {
                if (u % 2 !== 0) continue;

                console.log(`${h} ${t} ${u}`);
            }
        }
    }
}

// solve(3, 5, 5);

