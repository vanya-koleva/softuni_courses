function solve(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    const helmetBreaks = Math.floor(lostFights / 2);
    const swordBreaks = Math.floor(lostFights / 3);
    const shieldBreaks = Math.floor(lostFights / 6);
    const armorBreaks = Math.floor(shieldBreaks / 2);

    const totalCost =
        helmetBreaks * helmetPrice +
        swordBreaks * swordPrice +
        shieldBreaks * shieldPrice +
        armorBreaks * armorPrice;

    console.log(`Gladiator expenses: ${totalCost.toFixed(2)} aureus`);
}

// solve(23, 12.5, 21.5, 40, 200);

