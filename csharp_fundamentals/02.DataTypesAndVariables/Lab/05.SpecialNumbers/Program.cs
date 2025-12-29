int n = int.Parse(Console.ReadLine());

List<int> specialSums = new() { 5, 7, 11 };

for (int i = 1; i <= n; i++)
{
    bool isSpecialNum = false;
    int sumOfDigits = 0;
    int number = i;

    while (number > 0)
    {
        sumOfDigits += number % 10;
        number /= 10;
    }

    if (specialSums.Contains(sumOfDigits))
    {
        isSpecialNum = true;
    }
    
    Console.WriteLine($"{i} -> {isSpecialNum}");
}