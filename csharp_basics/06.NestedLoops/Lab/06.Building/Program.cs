namespace _06.Building;

class Program
{
    static void Main(string[] args)
    {
        int floors = int.Parse(Console.ReadLine());
        int rooms = int.Parse(Console.ReadLine());

        string floorLetter = "";

        for (int floor = floors; floor > 0; floor--)
        {
            if (floor == floors)
            {
                floorLetter = "L";
            }
            else if (floor % 2 == 0)
            {
                floorLetter = "O";
            }
            else
            {
                floorLetter = "A";
            }

            for (int room = 0; room < rooms; room++)
            {
                Console.Write($"{floorLetter}{floor}{room} ");
            }
            
            Console.WriteLine("");
        }
    }
}