function solve(input) {
    const searchedBook = input.shift();
    let checkedBooks = 0;

    while (true) {
        let currentBook = input.shift();

        if (currentBook === 'No More Books') {
            console.log('The book you search is not here!');
            console.log(`You checked ${checkedBooks} books.`);
            break;
        }

        if (currentBook === searchedBook) {
            console.log(`You checked ${checkedBooks} books and found it.`);
            break;
        }

        checkedBooks++;
    }
}

solve(['Troy', 'Stronger', 'Life Style', 'Troy']);

