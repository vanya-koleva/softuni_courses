# While Loop

## Revision

```js
for (let i = 1; i <= 3; ) {
    console.log(i);
}
// infinite loop

for (;;) {
    console.log('SoftUni');
}
// infinite loop

for (let i = 0; i < 2; i += 0.5) {
    console.log(i + ', ');
}
// 0, 0.5, 1, 1.5
```

## While Loop

```js
while (...){
   //code
}
```

`break` to break the loop.  
`continue` to the next iteration of the loop.

## Min / Max Numbers

-   **`Number.MIN_SAFE_INTEGER`** – The smallest safe integer: `-9007199254740991`
-   **`Number.MAX_SAFE_INTEGER`** – The largest safe integer: `9007199254740991`

-   Beyond this range, JavaScript cannot guarantee precision, meaning calculations may produce unexpected results:

```js
console.log(9007199254740991 + 1); // 9007199254740992 (correct)
console.log(9007199254740991 + 2); // 9007199254740992 (incorrect!)
```

-   **`Number.NEGATIVE_INFINITY`**, **`Number.POSITIVE_INFINITY`** - always larger or smaller than any other number.

```js
console.log(Number.POSITIVE_INFINITY); // Infinity
console.log(Number.NEGATIVE_INFINITY); // -Infinity
```

