using System;
using Microsoft.VisualBasic;
class _0006_Rendom
{
    public static void Main()
    {
        Console.WriteLine("Hello, Lets revise console.WriteLine and Write");
        Console.Write("Create a random number between 1 and 100: \n");
        var _randomNumber = new Random();
        Random dice =  new Random();
        for (int i = 0; i < 10; i++)
        {
            Console.Write(_randomNumber.Next(1, 100) + "\t");
            Console.WriteLine(dice.Next(1,7));
        }
        

    }


}