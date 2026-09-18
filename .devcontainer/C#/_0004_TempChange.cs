using System;
class Program
{
    public static void Main()
    {
        //int _Fahrenheit = int.Parse(Console.Read());
        Console.WriteLine(5/10);
        Console.WriteLine("Windows" +1 +1);
        double _temp = double.Parse(Console.ReadLine());
        Console.WriteLine($"You entered: {_temp}");
        //double celsius = (_temp - 32m) *(5m/9m);
        double celsius = (_temp - 32.0) *(5.0/9.0);
        decimal celsius1 = ((decimal)_temp - 32m) *(5m/9m);
        Console.WriteLine($"Temp in Celsius is, {celsius} and {celsius1}");

    }
}