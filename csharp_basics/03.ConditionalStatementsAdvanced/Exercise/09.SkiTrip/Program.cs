int days = int.Parse(Console.ReadLine());
string accomodation = Console.ReadLine();
string grade = Console.ReadLine();

const double roomPrice = 18.00;
const double appartmentPrice = 25.00;
const double presidentPrice = 35.00;

int nights = days - 1;
double price = 0.0;

switch (accomodation)
{
    case "apartment":
        price = appartmentPrice * nights;
        
        if (days < 10)
        {
            price *= 0.7;
        }
        else if (days <= 15)
        {
            price *= 0.65;
        }
        else
        {
            price *= 0.5;
        }
        break;
    
    case "president apartment":
        price = presidentPrice * nights;
        
        if (days < 10)
        {
            price *= 0.9;
        }
        else if (days <= 15)
        {
            price *= 0.85;
        }
        else
        {
            price *= 0.8;
        }
        break;
        
    default:
        price = roomPrice * nights;
        break;
}

if (grade == "positive")
{
    price *= 1.25;
}
else
{
    price *= 0.9;
}

Console.WriteLine($"{price:F2}");
