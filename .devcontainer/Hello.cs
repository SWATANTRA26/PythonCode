using System;
class program 
{
    static void Main()
    {
        Console.WriteLine("Hello, Welcome to C#!");
        Console.Write("Hello, Welcome to C#!");
        Console.Write("Hi checking line change");
        /*
        we can print hello world in c# without using "using System;" and "class Program" 
        and "static void Main()". But it is not a good practice to do so.         */
        Console.WriteLine();
        Console.WriteLine(123);
        Console.WriteLine(0.25F);
        Console.WriteLine(12.25);

        char userOption = 'A'; 
        Console.WriteLine(userOption);
    
        int gameScore = 100;
        Console.WriteLine(gameScore);

        decimal particlesPerMillion = 12.5M;
        Console.WriteLine(particlesPerMillion);

        bool processedCustomer = true;
        Console.WriteLine(processedCustomer);
// var keyword is used to declare a variable without specifying its type explicitly. The type is inferred from the assigned value.
        var name ="SWATANTRA";
        Console.WriteLine(name);

        var age = 25;
        Console.WriteLine(age);
    }
}
