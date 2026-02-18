namespace _03.RoundingNumbers;

class Program
{
    static void Main(string[] args)
    {
        double[] nums =  Console.ReadLine()
            .Split()
            .Select(double.Parse)
            .ToArray();
        
        int[] newNums = new int[nums.Length];

        for (int i = 0; i < nums.Length; i++)
        {
            newNums[i] = (int)Math.Round(nums[i], MidpointRounding.AwayFromZero);
            Console.WriteLine($"{nums[i]} => {newNums[i]}");
        }
    }
}