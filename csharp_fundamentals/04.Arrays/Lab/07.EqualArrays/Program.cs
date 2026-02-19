using System.ComponentModel.Design;

namespace _07.EqualArrays;

class Program
{
    static void Main(string[] args)
    {
        int[] nums1 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int[] nums2 = Console.ReadLine().Split().Select(int.Parse).ToArray();

        for (int i = 0; i < nums1.Length; i++)
        {
            if (nums1[i] != nums2[i])
            {
                Console.WriteLine($"Arrays are not identical. Found difference at {i} index");
                return;
            }
        }
        
        Console.WriteLine($"Arrays are identical. Sum: {nums1.Sum()}");
    }
}