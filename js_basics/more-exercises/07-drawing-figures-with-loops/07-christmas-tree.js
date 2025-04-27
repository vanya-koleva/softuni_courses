function solve(n) {
    console.log(' '.repeat(n) + ' | ');
    
    for (let i = 1; i <= n; i++) {
        const stars = '*'.repeat(i)
        const spaces = ' '.repeat(n - i)
        console.log(spaces + stars + ' | ' + stars);
    }
}

