﻿int hours = int.Parse(Console.ReadLine());
int minutes = int.Parse(Console.ReadLine());

minutes += 15;

if (minutes >= 60)
{
    hours++;
    minutes -= 60;
}

if (hours >= 24)
{
    hours = 0;
}

Console.WriteLine($"{hours}:{minutes:D2}");
    