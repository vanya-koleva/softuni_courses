int nylon = int.Parse(Console.ReadLine());
int paint = int.Parse(Console.ReadLine());
int thinner = int.Parse(Console.ReadLine());
int hours = int.Parse(Console.ReadLine());

double pricePerNylon = 1.5;
double pricePerPaint = 14.5;
double pricePerThinner = 5;
double priceOfBags = 0.4;

double totalNylon = (nylon + 2) * pricePerNylon;
double totalPaint = (paint * 1.1) * pricePerPaint;
double totalMaterialsPrice = totalNylon + totalPaint + thinner * pricePerThinner + priceOfBags;
double workersPrice = (totalMaterialsPrice * 0.3) * hours;

double totalPrice = totalMaterialsPrice + workersPrice;
Console.WriteLine(totalPrice);
