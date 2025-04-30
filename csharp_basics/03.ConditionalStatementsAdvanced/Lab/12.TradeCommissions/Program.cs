string city = Console.ReadLine();
double sales = double.Parse(Console.ReadLine());

bool validInput = true;
double commission = 0;

switch (city)
{
    case "Sofia":
        if (sales is >= 0 and <= 500)
        {
            commission = 0.05;
        } else if (sales is > 500 and <= 1000)
        {
            commission = 0.07;
        } else if (sales is > 1000 and <= 10000)
        {
            commission = 0.08;
        } else if (sales > 10000)
        {
            commission = 0.12;
        }
        else
        {
            validInput = false;
        }
        break;
    case "Varna":
        if (sales is >= 0 and <= 500)
        {
            commission = 0.045;
        } else if (sales is > 500 and <= 1000)
        {
            commission = 0.075;
        } else if (sales is > 1000 and <= 10000)
        {
            commission = 0.1;
        } else if (sales > 10000)
        {
            commission = 0.13;
        }
        else
        {
            validInput = false;
        }
        break;
    case "Plovdiv":
        if (sales is >= 0 and <= 500)
        {
            commission = 0.055;
        } else if (sales is > 500 and <= 1000)
        {
            commission = 0.08;
        } else if (sales is > 1000 and <= 10000)
        {
            commission = 0.12;
        } else if (sales > 10000)
        {
            commission = 0.145;
        }
        else
        {
            validInput = false;
        }
        break;
    default:
        validInput = false;
        break;
}

Console.WriteLine(!validInput ? "error" : $"{sales * commission:F2}");
