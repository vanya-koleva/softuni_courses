int hour = int.Parse(Console.ReadLine());
string day = Console.ReadLine();

bool isWorkingDay = day is "Monday" or "Tuesday" or "Wednesday"
                        or "Thursday" or "Friday" or "Saturday";
bool isWorkingHour = hour is >= 10 and <= 18;

if (isWorkingDay && isWorkingHour)
{
    Console.WriteLine("open");
}
else
{
    Console.WriteLine("closed");
}
