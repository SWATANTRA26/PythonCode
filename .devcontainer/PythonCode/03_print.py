# Print is output statement in python language 
print("String")
print(3*"Hi")
print(3*"\n Hi this is swatantra ")
# Operator "+" concenate string
print("Hi"+"My name is Swatantra"+"Sorry i know you know")
a,b,c = 2,3,40
print(a,b,c)

# Below commands are working fine with terminal and run with terminal 
print(a,b,c, sep=",") # Seprate a b c with whatever you want
print(a,b,c, sep="---")
print(a,b,c, sep=" Ho ")
print("Hello", end="\t")
print("Swatantra",end="\t")
print('What you want', end='')

#Print number and string 
print( a, "is an even number and ",b, "is a odd number " )

# Use of print with formatted string 
x,y,z= 2,14.55,'Singh'

print(type(x))
print(type(y))
print(type(z))
print('x is = %i', y)
print('a is = %d', y)
print('a is ={0}'.format(x))

print(type(y))

# Print with  {}  we can formate values what we need to display 
P= [10,55,63,'Test1','Test2']
Q=200
R=300
S=500
print('P1 is {0}'.format(P[3]))
print('Q is {0}, R is {1}, S is {2}'.format(Q,R,S))
print('Q is {0}, R is {1}, S is {2}'.format(Q,S,R))
print('Q is {0}, R is {1}, S is {2}'.format(S,R,Q))


print('Q is {0}, R is {1}, S is {2}'.format(Q,R,S))
print('Q is {1}, R is {0}, S is {2}'.format(Q,R,S))
print('Q is {1}, R is {2}, S is {0}'.format(Q,R,S))

# A very good example  of above formate is showing salary
Name, Sal = "Swatantra", 50000
print("Hi {0}, Your Salary is {1}".format(Name, Sal))
