string month = Console.ReadLine();
int nights = int.Parse(Console.ReadLine());

double studioPricePerNight = 0.0;
double apartmentPricePerNight = 0.0;
double studioTotalPrice;
double apartmentTotalPrice;

switch (month)
{
    case "May":
    case "October":
        studioPricePerNight = 50;
        apartmentPricePerNight = 65;

        if (nights > 14)
        {
            studioPricePerNight *= 0.7;
        }
        else if (nights > 7)
        {
            studioPricePerNight *= 0.95;
        }
        break;

    case "June":
    case "September":
        studioPricePerNight = 75.20;
        apartmentPricePerNight = 68.70;

        if (nights > 14)
        {
            studioPricePerNight *= 0.8;
        }
        break;

    case "July":
    case "August":
        studioPricePerNight = 76;
        apartmentPricePerNight = 77;
        break;
}

studioTotalPrice = studioPricePerNight * nights;
apartmentTotalPrice = apartmentPricePerNight * nights;

if (nights > 14)
{
    apartmentTotalPrice *= 0.9;
}

Console.WriteLine($"Apartment: {apartmentTotalPrice:F2} lv.");
Console.WriteLine($"Studio: {studioTotalPrice:F2} lv.");
