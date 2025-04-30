string fruit = Console.ReadLine();
string day = Console.ReadLine();
double quantity = double.Parse(Console.ReadLine());

double fruitPrice = 0;
bool validInput = true;

switch (day)
{
    case "Monday":
    case "Tuesday":
    case "Wednesday":
    case "Thursday":
    case "Friday":
        switch (fruit)
        {
            case "banana":
                fruitPrice = 2.5;
                break;
            case "apple":
                fruitPrice = 1.2;
                break;
            case "orange":
                fruitPrice = 0.85;
                break;
            case "grapefruit":
                fruitPrice = 1.45;
                break;
            case "kiwi":
                fruitPrice = 2.7;
                break;
            case "pineapple":
                fruitPrice = 5.5;
                break;
            case "grapes":
                fruitPrice = 3.85;
                break;
            default:
                validInput = false;
                break;
        }
        break;
    case "Saturday":
    case "Sunday":
        switch (fruit)
        {
            case "banana":
                fruitPrice = 2.7;
                break;
            case "apple":
                fruitPrice = 1.25;
                break;
            case "orange":
                fruitPrice = 0.90;
                break;
            case "grapefruit":
                fruitPrice = 1.60;
                break;
            case "kiwi":
                fruitPrice = 3;
                break;
            case "pineapple":
                fruitPrice = 5.6;
                break;
            case "grapes":
                fruitPrice = 4.2;
                break;
            default:
                validInput = false;
                break;
        }
        break;
    default:
        validInput = false;
        break;
}

Console.WriteLine(!validInput ? "error" : $"{fruitPrice * quantity:F2}");
