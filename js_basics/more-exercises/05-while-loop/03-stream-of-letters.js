function solve(input) {
    let word = '';
    let text = '';

    let cCounter = 0;
    let oCounter = 0;
    let nCounter = 0;

    while (input.length > 0) {
        if (cCounter === 1 && oCounter === 1 && nCounter === 1) {
            text += `${word} `;
            word = '';
            cCounter = 0;
            oCounter = 0;
            nCounter = 0;
        }

        const char = input.shift();

        if (char === 'End') {
            break;
        }

        const code = char.charCodeAt(0);

        const isLetter = (code >= 65 && code <= 90) || (code >= 97 && code <= 122);

        if (!isLetter) {
            continue;
        }

        if (char === 'c' && cCounter === 0) {
            cCounter++;
            continue;
        } else if (char === 'o' && oCounter === 0) {
            oCounter++;
            continue;
        } else if (char === 'n' && nCounter === 0) {
            nCounter++;
            continue;
        }

        word += char;
    }

    if (cCounter === 1 && oCounter === 1 && nCounter === 1) {
        text += `${word} `;
    }

    console.log(text);
}

// solve([
//     'H',
//     'n',
//     'e',
//     'l',
//     'l',
//     'o',
//     'o',
//     'c',
//     't',
//     'c',
//     'h',
//     'o',
//     'e',
//     'r',
//     'e',
//     'n',
//     'e',
//     'End',
// ]);

