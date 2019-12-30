#KJC4 4CREDITS
def sumN(n):
    sum = 0
    for num in range(1,n+1):
        sum = num + sum
    return sum

def sumNCubes(n):
    cubes_sum = 0
    for num in range(1,n+1):
        num = num ** 3
        cubes_sum = num + cubes_sum
    return cubes_sum



print("This program finds the sum of the first n natural numbers")
print("This program also finds the sum of the cubes of the first n natural numbers")
user_input = eval((input("please input your n:")))
natural_sum = sumN(user_input)
cubes_sum = sumNCubes(user_input)
print("the sum of the first", user_input, "natural numbers is ", natural_sum)
print ("the sum of the cubes of the first" , user_input, "natural numbers is", cubes_sum)
