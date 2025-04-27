double excursionPrice = double.Parse(Console.ReadLine());
int puzzlesNum = int.Parse(Console.ReadLine());
int dollsNum = int.Parse(Console.ReadLine());
int bearsNum = int.Parse(Console.ReadLine());
int minionsNum = int.Parse(Console.ReadLine());
int trucksNum = int.Parse(Console.ReadLine());

double puzzlesPrice = puzzlesNum * 2.6;
double dollsPrice = dollsNum * 3;
double bearsPrice = bearsNum * 4.1;
double minionsPrice = minionsNum * 8.2;
double trucksPrice = trucksNum * 2;

double price = puzzlesPrice + dollsPrice + bearsPrice + minionsPrice + trucksPrice;
int toysNum = puzzlesNum + dollsNum + bearsNum + minionsNum + trucksNum;

if (toysNum >= 50)
{
    price *= 0.75;
}

double totalSum = price * 0.9;
double difference = Math.Abs(excursionPrice - totalSum);

if (totalSum >= excursionPrice)
{
    Console.WriteLine($"Yes! {difference:f2} lv left.");
}
else
{
    Console.WriteLine($"Not enough money! {difference:f2} lv needed.");
}
