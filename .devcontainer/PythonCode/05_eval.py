#Test Eval() function 
# Eval function take string and 
a, b =5,10
res =eval("a+b-4")
print(res)

# Eval with input
x=eval(input("Enter an expression : "))
print(x)

# Can we input list with below expression we can input content which will store in list 
#a= [int(x) for x in input("Enter n Number : ").split()]
# One more method with eval()
lst=eval(input('Enter a list = '))
# Enter values inside []
tpl=eval(input('Enter a Tuple = '))
#Enter tuple inside ()
print(lst)
print(tpl)