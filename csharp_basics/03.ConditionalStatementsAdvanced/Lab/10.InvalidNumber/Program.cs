int num = int.Parse(Console.ReadLine());

if ((num is < 100 or > 200) && num != 0)
{
    Console.WriteLine("invalid");
}
