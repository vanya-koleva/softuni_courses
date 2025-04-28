string dramaName = Console.ReadLine();
int episodeDuration = int.Parse(Console.ReadLine());
int breakDuration = int.Parse(Console.ReadLine());

double lunchDuration = breakDuration / 8d;
double leisureDuration = breakDuration / 4d;
double freeTime = breakDuration - lunchDuration - leisureDuration;

double difference = Math.Abs(episodeDuration - freeTime);

if (freeTime >= episodeDuration)
{
    Console.WriteLine($"You have enough time to watch {dramaName} and left with {Math.Ceiling(difference)} minutes free time.");
}
else
{
    Console.WriteLine($"You don't have enough time to watch {dramaName}, you need {Math.Ceiling(difference)} more minutes.");
}
