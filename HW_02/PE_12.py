#PE12
#KJC4 4 CREDITS
def main() :
    total_sum = 0
    print("This will help you find the sum of the cubes of the first n natural numbers")
    nat= eval((input("please input your n:")))
    for num in range(1,nat+1):
        num = num ** 3
        total_sum = num + total_sum
    print("the sum is" ,total_sum)

main()
