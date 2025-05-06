const text = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iusto libero quam reprehenderit voluptatem laborum, quidem, cumque optio eos beatae delectus veritatis totam, cupiditate Iste laboriosam doloribus! Eos labore suscipit Autem!';

// Regular Expressions literal
const pattern = /([A-Z])[a-z]+/g;

// RegExp class
const pattern2 = new RegExp('[A-Z][a-z]+', 'g');

// -- REGEX METHODS --
// Test method
const result = pattern.test(text);
console.log(result);

// Exec method
const execResult = pattern.exec(text);
console.log(execResult);
console.log(pattern.exec(text));
console.log(pattern.exec(text));

// -- STRING METHODS --
// Match
console.log('Match--');
const matchResult = text.match(pattern);
console.log(matchResult);

// Match ALl
console.log('--Match All');
const matchAllResult = text.matchAll(pattern);
for (const match of matchAllResult) {
    console.log(match);
}

// Replace
let replacedText = text.replace(pattern, '****');
console.log(replacedText);

// Split
let input = 'first.second/third|fouth';
const words = input.split(/[\.\/|]/g);
console.log(words);
