// Literals
const singleQuoteLiteral = 'text';
const doubleQuoteLiteral = "text";
const templateLiteral = `Some longer ${singleQuoteLiteral}`; // Don't use it without interpolation

// Escaping
const quoteText = 'quote: "Some Fancy Quote"';
const singleQuoteText = "K'vo staa!";
const escapeCharacters = 'quote: \'Some Fancy Quote\'';
console.log(escapeCharacters);

// Concatenation operator
const firstString = 'Hi!';
const secondString = 'My name is Ivo';
const greet = firstString + secondString;
console.log(greet);

// Concatenation method
console.log(firstString.concat(secondString));

// IndexOf - Find index of substring
const text = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Laborum placeat debitis praesentium est aut libero quam cum, quibusdam sunt vitae ab, dolor ipsa at id nobis numquam quos commodi soluta totam!';
const firstDolorIndex = text.indexOf('dolor');
const lastDolorIndex = text.lastIndexOf('dolor');

// Substring
const subText = text.substring(0, firstDolorIndex);
console.log(subText);

// Replace
const replacedDolorText = text.replace('dolor', '*****');
console.log(replacedDolorText);

const replacedDolorAllText = text.replaceAll('dolor', '*****');
console.log(replacedDolorAllText);

// Split string into an array
const loremArray = text.split(' ');
console.log(loremArray);

// Includes - check for substring
const hasDolor = text.includes('dolor');
console.log(hasDolor);

// Repeat string
console.log('Tro' + 'lo'.repeat(10));

// Trim
const stringWithSpaces = '  some  text  ';
console.log(stringWithSpaces);
console.log(stringWithSpaces.trimEnd());
console.log(stringWithSpaces.trimStart());
console.log(stringWithSpaces.trim());
console.log(stringWithSpaces.trim().replace('  ', ' '));

// StartWith EndsWith
console.log(text.startsWith('Lorem'));
console.log(text.endsWith('Ipsum'));

// Pad start string
let number = 10;
let binaryString = number.toString(2);
console.log(binaryString.padStart(8, '0'));

// Pad endstring
let decimalNumber = 0.111;
console.log(decimalNumber.toString().padEnd(8, '0'));
