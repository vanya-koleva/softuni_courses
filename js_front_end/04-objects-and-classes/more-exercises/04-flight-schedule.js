function solve(input) {
    const [allFlights, changedStatuses, statusToCheck] = input;

    const flights = {};

    allFlights.forEach(flight => {
        const [flightNum, ...destinationParts] = flight.split(' ');
        const destination = destinationParts.join(' ');
        flights[flightNum] = {
            Destination: destination,
            Status: 'Ready to fly',
        };
    });

    changedStatuses.forEach(update => {
        const [flightNum, newStatus] = update.split(' ');

        if (flights[flightNum]) {
            flights[flightNum].Status = newStatus;
        }
    });

    const checkedStatus = statusToCheck[0];

    for (const flight in flights) {
        if (flights[flight].Status === checkedStatus) {
            console.log(flights[flight]);
        }
    }
}

