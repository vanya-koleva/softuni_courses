double budget = double.Parse(Console.ReadLine());
string season = Console.ReadLine();

string destination = "";
string accomodation = "";
double percent = 0.0;

switch (season)
{
    case "summer":
        accomodation = "Camp";
        break;
    default:
        accomodation = "Hotel";
        break;
}

if (budget <= 100)
{
    destination = "Bulgaria";
    
    if (season == "summer")
    {
        percent = 0.3;
    }
    else
    {
        percent = 0.7;
    }
}
else if (budget <= 1000)
{
    destination = "Balkans";
    
    if (season == "summer")
    {
        percent = 0.4;
    }
    else
    {
        percent = 0.8;
    }
}
else
{
    destination = "Europe";
    percent = 0.9;
    accomodation = "Hotel";
}

double price = budget * percent;

Console.WriteLine($"Somewhere in {destination}");
Console.WriteLine($"{accomodation} - {price:F2}");
