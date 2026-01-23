string productName = Console.ReadLine();
int quantity = int.Parse(Console.ReadLine());

static string GetPrice(string product, int qty)
{
    var prices = new Dictionary<string, double>
    {
        ["coffee"] = 1.50,
        ["water"] = 1.00,
        ["coke"] = 1.40,
        ["snacks"] = 2.00
    };
    
    double totalPrice = prices[product]  * qty;
    return totalPrice.ToString("F2");
}

static void PrintPrice(string product, int qty)
{
    Console.WriteLine(GetPrice(product, qty));
}

PrintPrice(productName,  quantity);
