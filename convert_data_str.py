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

