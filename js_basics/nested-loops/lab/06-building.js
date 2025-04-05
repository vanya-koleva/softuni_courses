function solve(floors, rooms) {
    floors = Number(floors);
    rooms = Number(rooms);

    for (let floor = floors; floor > 0; floor--) {
        let result = '';

        for (let room = 0; room < rooms; room++) {
            if (floor == floors) {
                result += `L${floor}${room} `;
            } else if (floor % 2 == 0) {
                result += `O${floor}${room} `;
            } else {
                result += `A${floor}${room} `;
            }
        }

        console.log(result);
    }
}

// solve(6, 4);

