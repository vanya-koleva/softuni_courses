function solve(lastSector, rowsInFirstSector, seatsOnOddRow) {
    const FIRST_SECTOR_CODE = 'A'.charCodeAt(0);
    const FIRST_SEAT_CODE = 'a'.charCodeAt(0);

    let totalSeats = 0;

    for (let s = FIRST_SECTOR_CODE; s <= lastSector.charCodeAt(0); s++) {
        let sector = String.fromCharCode(s);
        let rows = rowsInFirstSector + (s - FIRST_SECTOR_CODE);

        for (let row = 1; row <= rows; row++) {
            let seats = row % 2 === 0 ? seatsOnOddRow + 2 : seatsOnOddRow;

            for (let seat = 0; seat < seats; seat++) {
                let seatLetter = String.fromCharCode(FIRST_SEAT_CODE + seat);

                console.log(`${sector}${row}${seatLetter}`);

                totalSeats++;
            }
        }
    }

    console.log(totalSeats);
}

// solve('B', 3, 2);

