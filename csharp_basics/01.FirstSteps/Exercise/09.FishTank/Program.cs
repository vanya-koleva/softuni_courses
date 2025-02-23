int volume = int.Parse(Console.ReadLine())
            * int.Parse(Console.ReadLine())
            * int.Parse(Console.ReadLine());

double percentage = double.Parse(Console.ReadLine()) * 0.01;

double volumeInLiters = volume * 0.001;
double freeSpace = volumeInLiters * (1 - percentage);

Console.WriteLine(freeSpace);
