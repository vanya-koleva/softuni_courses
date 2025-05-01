int budget = int.Parse(Console.ReadLine());
string season = Console.ReadLine();
int fishermenCount = int.Parse(Console.ReadLine());

const int springPrice = 3000;
const int summerAndAutumnPrice = 4200;
const int winterPrice = 2600;

const double discountSmall = 0.9;
const double discountMedium = 0.85;
const double discountLarge = 0.75;
const double discountExtra = 0.95;

double price = 0;

switch (season)
{
    case "Spring":
        price = springPrice;
        break;
    case "Summer":
    case "Autumn":
        price = summerAndAutumnPrice;
        break;
    default:
        price = winterPrice;
        break;
}

if (fishermenCount <= 6)
{
    price *= discountSmall;
}
else if (fishermenCount <= 11)
{
    price *= discountMedium;
}
else
{
    price *= discountLarge;
}

if (season != "Autumn" && fishermenCount % 2 == 0)
{
    price *= discountExtra;
}

double difference = Math.Abs(budget - price);

if (budget >= price)
{
    Console.WriteLine($"Yes! You have {difference:F2} leva left.");
}
else
{
    Console.WriteLine($"Not enough money! You need {difference:F2} leva.");
}
