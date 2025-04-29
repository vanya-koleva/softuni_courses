string day = Console.ReadLine().Trim().ToLowerInvariant();

switch (day)
{
    case "monday":
    case "tuesday":
    case "friday":
        Console.WriteLine("12");
        break;
    case "wednesday":
    case "thursday":
        Console.WriteLine("14");
        break;
    case "saturday":
    case "sunday":
        Console.WriteLine("16");
        break;
    default:
        Console.WriteLine("Invalid day.");
        break;
}
