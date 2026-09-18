using System;
using System.Data;
class _0008_ifelse
{
    public static void Main()
    {
        Random dice1 = new Random();
        int roll1 = dice1.Next(1, 7);
        int roll2 = dice1.Next(1, 7);
        int roll3 = dice1.Next(1, 7);
        Console.WriteLine("You rolled: " + roll1 + ", " + roll2 + ", " + roll3);
        int total = roll1 + roll2 + roll3;
        for(int i=0; i<10; i++)
        {
            
            if (total >= 13)
            {
                Console.WriteLine("You win!");
            }
            else
            {
                Console.WriteLine("You lose!");
            }
        }
    }

}