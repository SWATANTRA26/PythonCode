using System;
class Program
{
    static void Main()
    {
        // Use + operator to add two numbers & concatenate strings 
        int a = 10, b = 20;
        int sum = a + b;
        Console.Write($"Sum of {a} and {b} is: {sum}\n");

        string str1 = "Hello, ";
        Console.WriteLine(str1 + sum);

        int sum1 = 20+25;
        int sub1 = 50-11;
        int qua1 = 10/7;
        double qua2 = 10.0/7.0;
        int rem1 = 10%7;
        Console.WriteLine($"Sum = {sum1} \n" +
                          $"Sub = {sub1} \n" +
                          $"Qua1 = {qua1} \n" +
                          $"Qua2 = {qua2} \n"+
                          $"Rem = {rem1}"); 

        Console.WriteLine($"Sum of 2 number is {sum1}, Sub of 2 number is {sub1}, Qua of 2 number is {qua1}, Qua of 2 number is {qua2} and Rem of 2 number is {rem1}");
    }

}