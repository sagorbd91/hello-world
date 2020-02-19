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

