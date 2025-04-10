function solve(height, length, heightTriangle) {
    const GREEN_PAINT_COVERAGE = 3.4;
    const RED_PAINT_COVERAGE = 4.3;
    const DOOR_AREA = 1.2 * 2;
    const WINDOW_AREA = 1.5 * 1.5;

    const backWall = height * height;
    const frontWall = backWall - DOOR_AREA;
    const sideWallsTotal = height * length * 2 - WINDOW_AREA * 2;
    const totalHouseArea = backWall + frontWall + sideWallsTotal;

    const roofRectangles = height * length * 2;
    const roofTriangles = 2 * (0.5 * height * heightTriangle);
    const totalRoofArea = roofRectangles + roofTriangles;

    const greenPaint = totalHouseArea / GREEN_PAINT_COVERAGE;
    const redPaint = totalRoofArea / RED_PAINT_COVERAGE;

    console.log(greenPaint.toFixed(2));
    console.log(redPaint.toFixed(2));
}

// solve(6, 10, 5.2);

