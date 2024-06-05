#Test While loop
# Use ctrl+/ to comment section of code 

# #Exercise 1
# x=1
# while x<100:
#     x+=1 #Increment x by 1
#     print(x)

#Exercise 2
# # Display Even number between 100 to 200
# x=100
# while x>=100 and x<200:
#     x+=2
#     print(x)


# #Exercise 3
# # Find Even number between two number 
# n1,n2=[int(x) for x in input("Enter 2 number : ").split(',')]
# print("Number 1 is {} and Number 2 is {}".format(n1,n2))
# # Check maximum amd min value 
# if n1>n2:
#     x=n2
#     # Is n2 is even
#     x1=x%2
#     if x1 != 0:
#         x=x+1
#     while x<n1:
#         x+=2
#         print("Even number between {0} and {1} is\t{2} ".format(n1,n2,x))
# else:
#     x=n1
#     # Is n1 is even
#     x1=x%2
#     if x1 !=0:
#         x=x+1
#     while x<n2:
#         x+=2
#         print("Even number between {0} and {1} is\t{2} ".format(n1,n2,x))

#Test from book to display even number between m and n
m,n = [int(i) for i in input('Enter minimum number and maximum ').split(',')]
x=m
if x%2 !=0:
    x=x+1
    while x>m and x<n:
        print(x)
        x+=2

if m>n:
    print("Please Enter minimum value first GAND na maraye")
