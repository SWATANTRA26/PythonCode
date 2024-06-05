#input() function is used to take input from keyboard 
# Take string as input and print same 

    #print("Please Enter a string")
    #str = input() # It will accept input till we press enter
    #print(str)

# We can pass string/massage inside input()
str1 = input("Enter your name :")
print("Name is {0},and type is {1}".format(str1, type(str1)))
#Even if we insert number it will store the value of input()
#in string charector is also consider as string

n1 = input("Enter your number:")
n2 = input("Enter your number:")
Sum = n1+n2     # This Sum concatenate string 
print("First Number is : {0}\t type{1}, \nSecond number is :{2}\t type{3}".format(n1, type(n1),n2,type(n2)))
print(Sum)
# To add we need to change formate 
n1,n2= int(n1),int(n2)
Sum = n1+n2
print("First Number is : {0}\t type{1}, \nSecond number is :{2}\t type{3}".format(n1, type(n1),n2,type(n2)))
print(Sum)

# How to take multiple input in same line 
a= [int(x) for x in input("Enter n Number : ").split()]  # This statement make a list name "a" and store the value 
# Since it is an int so we can't pass str as an input "Enter n Number : 2 m 6 5 jkk" will generate wrong result 
p,q,r= [int(x) for x in input("Enter 3 Number : ").split()]  # In this case if acceed more than 3 it will create issue 
print(a,type(a))
print(p,q,r)
#split() method separete the values where "Space " is found

# Can we input list with below expression we can input content which will store in list 
a= [int(x) for x in input("Enter n Number : ").split()]