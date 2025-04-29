int num = int.Parse(Console.ReadLine());

if (num is >= -100 and <= 100 && num != 0)
{
    Console.WriteLine("Yes");
}
else
{
    Console.WriteLine("No");
}
