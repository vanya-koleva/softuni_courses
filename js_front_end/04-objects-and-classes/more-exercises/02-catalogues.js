function solve(input) {
    let products = input.map(p => {
        const [name, price] = p.split(' : ');
        return { name, price: Number(price) };
    });

    products.sort((a, b) => a.name.localeCompare(b.name, undefined));

    let initial = '';

    for (let product of products) {
        let productInitial = product.name[0];

        if (productInitial !== initial) {
            console.log(productInitial);
            initial = productInitial;
        }

        console.log(`  ${product.name}: ${product.price}`);
    }
}

