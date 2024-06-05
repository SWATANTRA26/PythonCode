#Control_Statement 
# if condition:
#    Statement

x= int(input("Enter a number :"))
chk_pr=x%2
chk_pr1=x%3
chk_pr2=x%5
chk_pr3=x%7
if chk_pr ==0:
    print("Entered Number {0} is a Even Number = ".format(x))
elif chk_pr != 0:
    print("Entered Number {0} is a Odd Number = ".format(x))
else:
    print("Entered Number {0} is Zero = ".format(x))

