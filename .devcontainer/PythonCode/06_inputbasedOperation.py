#Program to take Two number and perform maths operation 
n1= int(input("Enter First Number = "))
n2= int(input("Enter Second Number = "))
Sum = n1+n2
Prod =n1*n2
Expo= n1**n2
Sub= n1-n2
Div= n1/n2

print('Sum of Number is :{0}\t DT{4}, \nSubtraction of Number is :{1}\t DT{5},\nProduct of Number is :{2}\t DT{6},\nExponent of Number is :{3}\t DT{7}'.format(Sum,Sub,Prod,Expo,type(Sum),type(Sub),type(Prod),type(Expo)))
print("Devision of Number is :  ",Div)


#One more Example to take number and add them 
a,b,c,d = [int(x) for x in input('Enter 4 number : ').split()]
print("Sum is = ", a+b+c+d)
