namespace _01.OldBooks;

class Program
{
    static void Main(string[] args)
    {
        string searchedBook = Console.ReadLine();
        int counter = 0;
        
        while (true)
        {
            string input = Console.ReadLine();
            
            if (input == searchedBook)
            {
                Console.WriteLine($"You checked {counter} books and found it.");
                break;
            }

            if (input == "No More Books")
            {
                Console.WriteLine("The book you search is not here!");
                Console.WriteLine($"You checked {counter} books.");
                break;
            }
            
            counter++;
        }
    }
}