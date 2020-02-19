# Square numbers in procedural way
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    print(result)

lst = [1,2,3,4,5]
my_nums = square_numbers
print(my_nums(lst))

###############################

# python generators

def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1,2,3,4,5,6])

print(my_nums) # it will make an object of generators
print(type(my_nums))

for num in my_nums:
    print(num)

#################################

# List Comprehension Method to pass the generator

my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)  # it will create a generator

for num in my_nums:
    print(num)




