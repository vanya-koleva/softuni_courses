double currentRecord = double.Parse(Console.ReadLine());
double distance = double.Parse(Console.ReadLine());
double timePerMeter = double.Parse(Console.ReadLine());

const double resistance = 12.5;

double delay = Math.Floor(distance / 15) * resistance;

double timeNeeded = distance * timePerMeter + delay;

if (timeNeeded < currentRecord)
{
    Console.WriteLine($"Yes, he succeeded! The new world record is {timeNeeded:f2} seconds.");
}
else
{
    double difference = timeNeeded - currentRecord;
    Console.WriteLine($"No, he failed! He was {difference:f2} seconds slower.");
}
