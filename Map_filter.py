#MAP Function
# here you will need to pass a list and a function to map the data

import math
radii = [2,5,6,7]
def area(r):
     return math.pi * (r**2)

x = list(map(area,radii))
print(x)

# Another Example
temps = [("berlin", 29), ("cairo", 45), ("dhaka", 30)]
c_to_f = lambda data:(data[0],9/5*data[1] +32)
#def celsious(x):
 #   for i in x:
 #       return i[0]*9/5 + 32
    
z = list(map(c_to_f,temps))
print(z)

# so in map function we will apply the function by iterating the data of list 

##############################################################3

# ZIP function

# list of dictionaries using zip function using 2 lists
# 2 list converted into list of dictionaries
color_name = ['red', 'maroon', 'yellow']
color_code = ['#0090', '#6887', '#6789']
name_with_code = [{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)]
print(name_with_code)


# Filter Function
#import statistics
data = [6.6,7.5,8.5]
def avg(data):
    return sum(data)/len(data)
#    print(y)
         
#avg(data)

value =list(filter(avg,data))
print(value)
