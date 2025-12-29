int number = int.Parse(Console.ReadLine());

Console.WriteLine(CheckSign(number));

static string CheckSign(int num)
{
    string result;

    if (num == 0)
    {
        result = $"The number {num} is zero. ";
    }
    else
    {
        result = $"The number {num} is {(num > 0 ? "positive" : "negative")}.";
    }
    
    return result;
}