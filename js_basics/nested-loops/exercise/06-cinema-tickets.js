function solve(input) {
    let studentTickets = 0;
    let standardTickets = 0;
    let kidTickets = 0;
    let index = 0;

    while (true) {
        let movieName = input[index++];

        if (movieName == 'Finish') {
            const totalTickets = studentTickets + standardTickets + kidTickets;
            const studentTicketsPercentage = (studentTickets / totalTickets) * 100;
            const standardTicketsPecentage = (standardTickets / totalTickets) * 100;
            const kidTicketsPercentage = (kidTickets / totalTickets) * 100;

            console.log(`Total tickets: ${totalTickets}`);
            console.log(`${studentTicketsPercentage.toFixed(2)}% student tickets.`);
            console.log(`${standardTicketsPecentage.toFixed(2)}% standard tickets.`);
            console.log(`${kidTicketsPercentage.toFixed(2)}% kids tickets.`);
            break;
        }

        let availablePlaces = Number(input[index++]);
        let ticketsSold = 0;

        for (let i = 0; i < availablePlaces; i++) {
            let ticketType = input[index++];

            if (ticketType == 'End') {
                break;
            }

            ticketsSold++;

            switch (ticketType) {
                case 'student':
                    studentTickets++;
                    break;
                case 'standard':
                    standardTickets++;
                    break;
                case 'kid':
                    kidTickets++;
                    break;
            }
        }

        let fullPercentage = (ticketsSold / availablePlaces) * 100;

        console.log(`${movieName} - ${fullPercentage.toFixed(2)}% full.`);
    }
}

// solve([
//     'Taxi',
//     '10',
//     'standard',
//     'kid',
//     'student',
//     'student',
//     'standard',
//     'standard',
//     'End',
//     'Scary Movie',
//     '6',
//     'student',
//     'student',
//     'student',
//     'student',
//     'student',
//     'student',
//     'Finish',
// ]);

