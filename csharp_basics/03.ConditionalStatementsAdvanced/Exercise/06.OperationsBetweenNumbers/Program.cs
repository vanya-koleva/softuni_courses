double num1 = int.Parse(Console.ReadLine());
double num2 = int.Parse(Console.ReadLine());
string operation = Console.ReadLine();

string operationString = $"{num1} {operation} {num2}";
double result = 0.0;

switch (operation)
{
    case "+":
        result = num1 + num2;
        Console.WriteLine($"{operationString} = {result} - {(result % 2 == 0 ? "even" : "odd")}");
        break;
    case "-":
        result = num1 - num2;
        Console.WriteLine($"{operationString} = {result} - {(result % 2 == 0 ? "even" : "odd")}");
        break;
    case "*":
        result = num1 * num2;
        Console.WriteLine($"{operationString} = {result} - {(result % 2 == 0 ? "even" : "odd")}");
        break;
    case "/":
        if (num2 != 0)
        {
            Console.WriteLine($"{operationString} = {num1 / num2:F2}");
        }
        else
        {
            Console.WriteLine($"Cannot divide {num1} by zero");
        }
        break;
    case "%":
        if (num2 != 0)
        {
            Console.WriteLine($"{operationString} = {num1 % num2}");
        }
        else
        {
            Console.WriteLine($"Cannot divide {num1} by zero");
        }
        break;
}
