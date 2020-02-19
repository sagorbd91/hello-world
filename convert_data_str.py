# Convert String to List to Tuple

"""
1. Create a Comma delimeted String
2. Convert it to a list
3. Convert the list to a tuple
"""

strx = "usa,canada,england,bangladesh"
print(strx)

# convert it to list

lsty = strx.split(",")
print(lsty)

# convert list to tuple

tupz = tuple(lsty)
print(tupz)

# convert tuple to list

lsta = list(tupz)
print(lsta)

# Convert list of tuple to dictionary

t = [("a", 1),("b", 2)]
for i in t:
    print(i)
    
dic = dict(t)
print(dic)

##############################

# Enumerate list and dictionary

example = ["north", "south", "east", "west", "left", "right"]

for i in range(len(example)):
        print(i, example[i])

for i, e in enumerate(example):
    print(i,e)

new_dict = dict(enumerate(example))
print(new_dict)


###############################
# Convert Dictionary from a list and count them

lis = [12,10,29,181,66,78]
my_dict ={}
for i in range(len(lis)):
        my_dict[lis[i]] = lis.count(lis[i])

print(my_dict)

#--------------------------------------------

products = ['a', 'b', 'c', 'd']
sales = [100,90,89,78,55]

product_sales = {"products": products, "sales": sales}
print(product_sales)

#------------------------------------------

# list of dictionaries using zip function using 2 lists
# 2 list converted into list of dictionaries
color_name = ['red', 'maroon', 'yellow']
color_code = ['#0090', '#6887', '#6789']
name_with_code = [{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)]
#name_with_code = [{f,c} for f,c in zip(color_name,color_code)]
print(name_with_code)

##########################################























