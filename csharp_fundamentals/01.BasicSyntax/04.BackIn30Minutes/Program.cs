int hours = int.Parse(Console.ReadLine());
int minutes = int.Parse(Console.ReadLine());

const int minutesPerHour = 60;
const int minutesToAdd = 30;

minutes += minutesToAdd;

if (minutes >= minutesPerHour)
{
    if (hours == 23)
    {
        hours = 0;
    }
    else
    {
        hours++;
    }

    minutes -= minutesPerHour;
}    

Console.WriteLine($"{hours}:{minutes:d2}");
