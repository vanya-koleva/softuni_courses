let cars = ['BMW', 'Audi', 'Mercedes', 'Toyota', 'Mazda'];

// Pop - remove last element (mutating)
let lastCar = cars.pop();
console.log(lastCar);
console.log(cars);

// Push - add element at the end (mutating)
cars.push('Mitsubishi');
console.log(cars);

// Push multiple elements
cars.push('Trabant', 'Lada');
console.log(cars);

// Shift - Remove first element (mutating) 
let firstCar = cars.shift();
console.log(cars);

// Unshift - Add element in the begining of the array (mutating)
cars.unshift('BMW');
console.log(cars);

// Splice Remove element at position (mutating) 
let removedCars = cars.splice(2, 1);
console.log(removedCars);
console.log(cars);

// Splice - add element on specific position (mutating)
cars.splice(4, 0, 'Mercedes');
console.log(cars);

// Reverse elements (mutating)
const reversedCars = cars.reverse();
console.log(reversedCars);
console.log(cars);
console.log(cars === reversedCars);

// Join array into a tring (non mutating)
let result = cars.join(', ');
console.log(result);

// Slice takes sub array (non mutating)
let middleCars = cars.slice(2, 5);
console.log(middleCars);
console.log(cars);
let endCars = cars.slice(4);
console.log(endCars);
let copyCars = cars.slice();
console.log(copyCars);
console.log(copyCars === cars);

// Reverse without mutation
let reversedCars2 = cars.slice().reverse();
console.log(reversedCars2);
console.log(cars);

// Includes - Check if element is in the array
const hasBmw = cars.includes('BMW');
console.log(hasBmw);
console.log(cars.includes('Chaika'));

// Includes check if elements is in the array after specified position
console.log(cars.includes('Toyota', 5));

// IndexOf - find index of element
const toyotaIndex = cars.indexOf('Toyota');
console.log(toyotaIndex);

// IndexOf - find index of not exisiting element // returns -1
const chaikaIndex = cars.indexOf('Chaika');
console.log(chaikaIndex);

// forEach - execute code for every element  (non mutating) (iterative)
cars.forEach(element => {
    console.log(element.toUpperCase());
});

// Map create new array with values based on original values (non mutating) (iterative)
const lowerCaseCars = cars.map(function(car) {
    return car.toLowerCase();
});
console.log(lowerCaseCars);

// Find - find the element (non mutating) (iterative)
let carWithL = cars.find(function(car) {
    return car.startsWith('L');
});
console.log(carWithL);

// Filter - find all elements based on condition  (non mutating) (iterative)
const carsWithT = cars.filter(function(car) {
    return car.startsWith('T');
});

console.log(carsWithT);
