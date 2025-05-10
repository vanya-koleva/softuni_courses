function solve(length) {
    const SEQUENCE = 'ATCGTTAGGG';
    let index = 0;

    const patterns = [
        (a, b) => `**${a}${b}**`,
        (a, b) => `*${a}--${b}*`,
        (a, b) => `${a}----${b}`,
        (a, b) => `*${a}--${b}*`,
    ];

    for (let i = 0; i < length; i++) {
        const getChars = () => {
            const a = SEQUENCE[index % SEQUENCE.length];
            const b = SEQUENCE[(index + 1) % SEQUENCE.length];
            index += 2;
            return [a, b];
        };

        const [char1, char2] = getChars();
        const line = patterns[i % 4](char1, char2);
        console.log(line);
    }
}

