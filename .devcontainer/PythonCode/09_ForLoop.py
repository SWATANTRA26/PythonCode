# Test for loop
# for var in sequence: 
#   Statement


# #Exercise 1
# str ="Swatantra"
# for i in str:
#     print(i)



# #Exercise 2
# a = input('Input a string :')
# for i in a:
#     print(i)


# #Exercise 3
# a = input('Input a string :')
# a1=len(a)
# for i in range(a1):
# #range(a1) will return value 0-a1 however we can modify minimum value range(x,a1)
#     print(a[i])


# #Exercise 4
# # Display odd number between two number 
# n1,n2=[int(i) for i in input("Enter min and max value separated by , :=").split(',')]
# #check min value is odd or make it odd
# if n1%2 ==0:
#     x=n1+1
# else:
#     x=n1
# for i in range(x,n2,2):
#     print(i)



# #Exercise 5
# # Display content of list 
# lst=[23,55,65,"Swatantra"]
# for i in lst:
#     print(i)

# #Exercise 6
# # Print sum of list 
# lst =[20,30,40,60]
# sum= 0
# for i in lst:
#     sum+=i
# print('Sum of list = ',sum)


# #Exercise 7
# #Print sum list input to an variable 
# a= [int(x) for x in input('Enter Number to add separated by ,').split(',')]
# sum= 0
# for i in a:
#     sum+=i
# print('Sum of list = ',sum)

#******************************************************************************************#
# **********Test on Nested loops **********************************************************#
# for i in range(1,11):
#     for j in range(1,i+1):
#         print('* ',end='') # End statement will not allow to go next line 
#     print()


# n=40
# for i in range(1,11):
#     print(' '*n, end='')
#     #print(' '*(n-1)+'* '*(i))
#     print('* ' *(i))
#     n-=1
# for j in range(1,11):
#     print('* '*n, end='')
#     #print(' '*(n-1)+'* '*(i))
#     print('' *(j))

# #Exercise check  prime number 
# a= int(input("Enter number to check prime number ="))
# x=0
# for i in range(1,a-1):
#     if a%i == 0:
#         x=x+1
#         #print(x)
#         continue
# if x==1:
#     print('{0} is a prime number'.format(a))
# else:
#     print('{0} is not a prime number'.format(a))



# # How many prime number we have till...
# a= int(input("Enter number  ="))
# for num in range(2,a+1):
#     #print(i)
#     for i in range(2,num):
#         if num%i == 0:
#             break
#         else:
#             print(num)


# Print febonachin
f1,f2=0,1
c=2
n=10
while c<n:
    f=f1+f2
    print(f,end=',')
    f1=f2
    f2=f
    c+=1
