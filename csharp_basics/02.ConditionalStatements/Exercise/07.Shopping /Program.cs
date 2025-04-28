double budget = double.Parse(Console.ReadLine());
int videoCardsNum = int.Parse(Console.ReadLine());
int processorsNum = int.Parse(Console.ReadLine());
int ramNum = int.Parse(Console.ReadLine());

const int VideoCardPrice = 250;
const double ProcessorPriceMultiplier = 0.35;
const double RamPriceMultiplier = 0.1;
const double DiscountMultiplier = 0.85;

int videoCardsTotal = videoCardsNum * VideoCardPrice;
double processorsTotal = processorsNum * videoCardsTotal * ProcessorPriceMultiplier;
double ramTotal = ramNum * videoCardsTotal * RamPriceMultiplier;

double totalPrice = videoCardsTotal + processorsTotal + ramTotal;

if (videoCardsNum > processorsNum)
{
    totalPrice *= DiscountMultiplier;
}

double difference = Math.Abs(totalPrice - budget);

if (budget >= totalPrice)
{
    Console.WriteLine($"You have {difference:F2} leva left!");
}
else
{
    Console.WriteLine($"Not enough money! You need {difference:F2} leva more!");
}
