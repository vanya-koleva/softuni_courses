double depositedSum = double.Parse(Console.ReadLine());
int monthsOfDeposit = int.Parse(Console.ReadLine());
double yearlyPercent = double.Parse(Console.ReadLine());

Console.WriteLine(depositedSum + monthsOfDeposit * (depositedSum * yearlyPercent / 100 / 12));
