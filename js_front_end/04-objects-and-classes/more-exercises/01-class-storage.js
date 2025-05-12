class Storage {
    constructor(capacity) {
        this.capacity = capacity;
        this.storage = [];
        this.totalCost = 0;
    }

    addProduct(product) {
        if (this.capacity >= product.quantity) {
            this.storage.push(product);
            this.capacity -= product.quantity;
            this.totalCost += product.price * product.quantity;
        }
    }

    getProducts() {
        return this.storage.map(p => JSON.stringify(p)).join('\n');
    }
}

