using System;
class _0009_ArrayUses
{
    public static void Main()
    {
        int[] numbers = new int[5];
        string[] _names = new string[3];
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;
        _names[0] = "Alice";
        _names[1] = "Bob";
        _names[2] = "Charlie";
        int sum = 0;
        int sum1 = 0;
        
        Console.WriteLine("Numbers array: " + numbers[0] + ", " + numbers[1] + ", " + numbers[2] + ", " + numbers[3] + ", " + numbers[4]);
        Console.WriteLine("Names array: " + _names[0] + ", " + _names[1] + ", " + _names[2]);
        
        string[] names = {"David", "Eve", "Frank"};
        foreach (string name in names)
        {
            Console.WriteLine(name);
        }

        int[] inventory = { 200, 450, 700, 175, 250 };
        foreach (int items in inventory)
        {
            Console.WriteLine(items);
            sum += items;
        }
        for(int i = 0; i < inventory.Length; i++)
        {
            Console.WriteLine(inventory[i]);
            sum1 += inventory[i]; 
        }
        Console.WriteLine("Total inventory: " + sum);
        Console.WriteLine("Updated inventory: " + sum1);
    }
}