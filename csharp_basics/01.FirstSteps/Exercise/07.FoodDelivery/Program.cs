int countChickenMenu = int.Parse(Console.ReadLine());
int countFishMenu = int.Parse(Console.ReadLine());
int countVegetarianMenu = int.Parse(Console.ReadLine());

double priceChickenMenu = 10.35;
double priceFishMenu = 12.4;
double priceVegetarianMenu = 8.15;
double priceDelivery = 2.50;

double price = countChickenMenu * priceChickenMenu + countFishMenu * priceFishMenu + countVegetarianMenu * priceVegetarianMenu;
double priceDessert = price * 0.2;
double totalPrice = price + priceDessert + priceDelivery;

Console.WriteLine(totalPrice);
