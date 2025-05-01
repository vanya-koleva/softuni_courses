string flowersType = Console.ReadLine();
int flowersCount = int.Parse(Console.ReadLine());
int budget = int.Parse(Console.ReadLine());

const double rosePrice = 5;
const double dahliasPrice = 3.8;
const double tulipsPrice = 2.8;
const double narcissusPrice = 3;
const double gladiolusPrice = 2.5;

double totalPrice = 0;

switch (flowersType)
{
    case "Roses":
        totalPrice = rosePrice * flowersCount;
        if (flowersCount > 80)
        {
            totalPrice *= 0.9;
        }
        break;
    case "Dahlias":
        totalPrice = dahliasPrice * flowersCount;
        if (flowersCount > 90)
        {
            totalPrice *= 0.85;
        }
        break;
    case "Tulips":
        totalPrice = tulipsPrice * flowersCount;
        if (flowersCount > 80)
        {
            totalPrice *= 0.85;
        }
        break;
    case "Narcissus":
        totalPrice = narcissusPrice * flowersCount;
        if (flowersCount < 120)
        {
            totalPrice *= 1.15;
        }
        break;
    case "Gladiolus":
        totalPrice = gladiolusPrice * flowersCount;
        if (flowersCount < 80)
        {
            totalPrice *= 1.2;
        }
        break;
}

double difference = Math.Abs(totalPrice - budget);

if (budget >= totalPrice)
{
    Console.WriteLine($"Hey, you have a great garden with " +
                      $"{flowersCount} {flowersType} and {difference:F2} leva left.");
}
else
{
    Console.WriteLine($"Not enough money, you need {difference:F2} leva more.");
}
