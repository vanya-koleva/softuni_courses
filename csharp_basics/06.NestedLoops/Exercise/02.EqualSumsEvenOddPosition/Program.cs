namespace _02.EqualSumsEvenOddPosition;

class Program
{
    static void Main(string[] args)
    {
        int start = int.Parse(Console.ReadLine());
        int end = int.Parse(Console.ReadLine());

        for (int i = start; i <= end; i++)
        {
            int oddSum = 0;
            int evenSum = 0;
            string numberAsStr = i.ToString();

            for (int j = 0; j < numberAsStr.Length; j++)
            {
                int digit = int.Parse(numberAsStr[j].ToString());

                if (j % 2 == 0)
                {
                    evenSum += digit;
                }
                else
                {
                    oddSum += digit;
                }
            }

            if (evenSum == oddSum)
            {
                Console.Write($"{i} ");
            }
        }
    }
}