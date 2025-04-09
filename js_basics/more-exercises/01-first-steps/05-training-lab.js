function solve(lenghtInMeters, widthInMeters) {
    const CORRIDOR_WIDTH = 100;
    const WORKING_SPACE_WIDTH = 70;
    const WORKING_SPACE_LENGTH = 120;
    const LOST_WORKING_SPACES = 3;

    const l = lenghtInMeters * 100;
    const w = widthInMeters * 100 - CORRIDOR_WIDTH;
    const totalLength = Math.floor(l / WORKING_SPACE_LENGTH);
    const totalWidth = Math.floor(w / WORKING_SPACE_WIDTH);

    const workingSpaces = totalLength * totalWidth - LOST_WORKING_SPACES;

    console.log(workingSpaces);
}

// solve(15, 8.9);

