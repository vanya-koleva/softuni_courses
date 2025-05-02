int examHour = int.Parse(Console.ReadLine());
int examMinutes = int.Parse(Console.ReadLine());
int arrivalHour = int.Parse(Console.ReadLine());
int arrivalMinutes = int.Parse(Console.ReadLine());

int examTime = examHour * 60 + examMinutes;
int arrivalTime = arrivalHour * 60 + arrivalMinutes;

int difference = Math.Abs(arrivalTime - examTime);
int hours = difference / 60;
int minutes = difference % 60;

if (arrivalTime > examTime)
{
    Console.WriteLine("Late");
    
    if (difference < 60)
    {
        Console.WriteLine($"{difference} minutes after the start");
    }
    else
    {
        Console.WriteLine($"{hours}:{minutes:D2} hours after the start");
    }
}
else if (arrivalTime < examTime - 30)
{
    Console.WriteLine("Early");
    
    if (difference < 60)
    {
        Console.WriteLine($"{difference} minutes before the start");
    }
    else
    {
        Console.WriteLine($"{hours}:{minutes:D2} hours before the start");
    }
}
else
{
    Console.WriteLine("On time");

    if (difference > 0)
    {
        Console.WriteLine($"{difference} minutes before the start");
    }
}
