# #pattern

# for i in range(1,11):
#     for j in range(1,11):
#         x=i*j
#         print(x,end=' \t')
#     print()


# #Above code can also be frame as 
# for i in range(1,11):
#     for j in range(1,11):
#         print('{:8}'.format(i*j),end='')
#     print()


# #In python we can use else with for loop and while loop unlike other language 
# for i in range(5):
#     print('Yes',end='\t')
# else:
#     print('No')
# #with the help of this we can generate output even if for loop is not executed make 5>0 in above code 

#print boarding pass of 10 people heaving PNR ['A','B','C','D','E','F','G','H','I','J','K']
#group1=[1,2,3,4,5,6]
group1=['A','B','C','D','E','F','G','H','I','J','K']
# Take care of datatype 
#PNR=int(input("Enter PNR number : "))
PNR=input("Enter PNR number : ")
for element in group1:
    if PNR == element:
        print('PNR found, please collect your boarding pass')
        break  #come out from loop
else:
    print("PNR Not found, please enter PNR No.")
