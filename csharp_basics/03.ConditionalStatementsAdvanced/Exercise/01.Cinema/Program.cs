string projectionType = Console.ReadLine();
int rows = int.Parse(Console.ReadLine());
int columns = int.Parse(Console.ReadLine());

const double premierePrice = 12.0;
const double normalPrice = 7.5;
const double discountPrice = 5.0;

double price = 0;

switch (projectionType)
{
    case "Premiere":
        price = premierePrice;
        break;
    case "Normal":
        price = normalPrice;
        break;
    case "Discount":
        price = discountPrice;
        break;
}

double total = price * rows * columns;

Console.WriteLine($"{total:F2} leva");
