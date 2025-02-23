int pens = int.Parse(Console.ReadLine());
int markers = int.Parse(Console.ReadLine());
int detergent = int.Parse(Console.ReadLine());
int discountPercentage = int.Parse(Console.ReadLine());

double pricePerPen = 5.8;
double pricePerMarker = 7.2;
double pricePerDetergent = 1.2; 

double totalSum = pens * pricePerPen + markers * pricePerMarker + detergent * pricePerDetergent;

Console.WriteLine(totalSum - (totalSum * discountPercentage / 100));
