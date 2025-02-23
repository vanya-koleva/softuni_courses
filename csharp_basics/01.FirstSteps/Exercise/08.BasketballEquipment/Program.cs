int yearlyFee = int.Parse(Console.ReadLine());

double sneakersPrice = yearlyFee * 0.6;
double outfitPrice = sneakersPrice * 0.8;
double ballPrice = outfitPrice * 0.25;
double accessoriesPrice = ballPrice * 0.2;
double totalPrice = yearlyFee + sneakersPrice + outfitPrice + ballPrice + accessoriesPrice;

Console.WriteLine(totalPrice);
