#Python provides some containers to store data, they are list, tupple 
# list start with [] "Square bracket" and tupple start with () pranthesis 
_list = [10,20,30,15.67,'Hello','welcome']
#for i in range(10):
#    print(_list[i])

print(_list)
_list.append("Hi") #Include 'hi' in the last 
print(_list)


# Work with tuple 
_tupple = (10,20,30,77,'hello','welcome')
print(_tupple)

#This shows tupple take less memory then list 
print(_list.__sizeof__())   #Outcome = 136
print(_tupple.__sizeof__()) #Outcome = 72




