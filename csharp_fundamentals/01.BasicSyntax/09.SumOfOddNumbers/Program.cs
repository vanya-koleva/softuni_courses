int n = int.Parse(Console.ReadLine());
int oddNum = 1;
int sum = 0;

for (int i = 1; i <= n; i++)
{
    Console.WriteLine(oddNum);
    sum += oddNum;
    oddNum += 2;
}

Console.WriteLine($"Sum: {sum}");
