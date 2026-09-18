using System;
class Program
{
    //By using "var" keyword, 
    /*
    static void Main()
    {
        var name = Console.ReadLine();
        var _msgCount = Console.ReadLine();
        var temp = Console.ReadLine();
        Console.WriteLine($"Hello {name}, you have {_msgCount} new messages and the temperature is {temp} degrees.");
    }
    */
    // Using different data type
    static void Main()
    {
        string name = Console.ReadLine();
        int _msgCount = int.Parse(Console.ReadLine());
        double temp = double.Parse(Console.ReadLine());
        Console.WriteLine($"Hello {name}, you have {_msgCount} messages in your inbox. The temperature is {temp} celsius.");

        int result = 3 + 1 * 5 /2;
        Console.WriteLine(result);

        decimal gradePointAverage = 3.99872831m;
        int roundedGPA = (int)gradePointAverage;
        Console.WriteLine(roundedGPA);

    }
} 