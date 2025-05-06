// Array literal
let names = ['Pesho', 'Gosho', 'Stamat'];

// Declare an empty array
let empty = [];

// Dynamic length
console.log(empty.length);
console.log(empty);
empty.length = 10;
console.log(empty.length);
console.log(empty);

// Mixed array
let mixed = ['Gosho', true, 20];
console.log(mixed);

// Dense array vs Sparse array
let denseArr = [undefined, undefined, undefined];
let sparseArr = [];
sparseArr.length = 3;

console.log(denseArr.length === sparseArr.length);
console.log(denseArr);
console.log(sparseArr);

// Number array
const numbers = [10, 20, 30, 40];

// Access elements (by index)
console.log(names[0]); // get first element
console.log(names[names.length - 1]); // get last element

// Access non existant element
console.log(names[30]);
console.log(names[-1]);

// Sparse array demo
const largeArray = [];
largeArray[1000] = 'Neshto';
largeArray[1001] = 'Drugo';
largeArray[0] = 'First';
console.log(largeArray.length);
console.log(largeArray);
console.log(largeArray[1000]);
console.log(largeArray[999]);

// Set element
names[0] = 'Peter'; // Update element
names[3] = 'Mariyka' // Add new element
names[names.length] = 'Ginka'; // Add element at the end
console.log(names);

// Array destructuring assignment
let [firstName, secondName, thirdName, fourthName] = names;
console.log(firstName);
console.log(secondName);
console.log(thirdName);
console.log(fourthName);
console.log(names); // Original array is untouched

// Partial destructuring
const [fName, sName] = names;
console.log(fName);
console.log(sName);

// Take the rest of the elements with partial destructuring using rest operator
const [first, second, ...restNames] = names;
console.log(first);
console.log(second);
console.log(restNames);

// iterate array with for
for (let i = 0; i < names.length; i++) {
    console.log(names[i]);
}

// Iterate array with for-of
console.log('ForOf ------');
for (const name of names) {
    console.log(name);
}
