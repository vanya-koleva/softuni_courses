double degrees = double.Parse(Console.ReadLine());
string timeOfDay = Console.ReadLine();

string outfit = "";
string shoes = "";

switch (timeOfDay)
{
    case "Morning":
        if (degrees is >= 10 and <= 18)
        {
            outfit = "Sweatshirt";
            shoes = "Sneakers";
        } 
        else if (degrees is > 18 and <= 24)
        {
            outfit = "Shirt";
            shoes = "Moccasins";
        } 
        else if (degrees is >= 25)
        {
            outfit = "T-Shirt";
            shoes = "Sandals";
        }
        break;
    case "Afternoon":
        if (degrees is >= 10 and <= 18)
        {
            outfit = "Shirt";
            shoes = "Moccasins";
        } 
        else if (degrees is > 18 and <= 24)
        {
            outfit = "T-Shirt";
            shoes = "Sandals";
        } 
        else if (degrees is >= 25)
        {
            outfit = "Swim Suit";
            shoes = "Barefoot";
        }
        break;
    default:
        outfit = "Shirt";
        shoes = "Moccasins";
        break;
}

Console.WriteLine($"It's {degrees} degrees, get your {outfit} and {shoes}.");
