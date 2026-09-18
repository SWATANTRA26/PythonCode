using System; //Used to access the Console class for input and output.
Console.WriteLine("Hello, Welcome to C#!");//Used to print.
class Program //Defines a class named Program, which is the entry point of the application.
{
    static void Main() //Defines the Main method, which is the entry point of the application. 
    // It is static, meaning it can be called without creating an instance of the Program class.
    {
        Console.WriteLine("Enter three numbers:");

        int[] numbers = new int[3];
        for (int i = 0; i < numbers.Length; i++)
        {
            Console.Write($"Number {i + 1}: ");
            if (!int.TryParse(Console.ReadLine(), out numbers[i]))
            {
                Console.WriteLine("Invalid input. Please enter an integer.");
                return;
            }
        }

        int sum = 0;
        for (int i = 0; i < numbers.Length; i++)
        {
            sum += numbers[i];
        }

        Console.WriteLine($"Sum = {sum}");

        if (sum > 50)
        {
            int maxValue = numbers[0];
            for (int i = 1; i < numbers.Length; i++)
            {
                if (numbers[i] > maxValue)
                    maxValue = numbers[i];
            }
            Console.WriteLine($"Sum is greater than 50. The highest value is {maxValue}.");
        }
        else
        {
            int minValue = numbers[0];
            for (int i = 1; i < numbers.Length; i++)
            {
                if (numbers[i] < minValue)
                    minValue = numbers[i];
            }
            Console.WriteLine($"Sum is not greater than 50. The lowest value is {minValue}.");
        }
    }
}