function solve(sentence) {
    const regex = /\w+/g;
    let words = sentence.match(regex) || [];

    let upperWords = words.map(word => word.toUpperCase()).join(', ');

    console.log(upperWords);
}

// solve('Hi, how are you?');

