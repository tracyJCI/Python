#KJC4 4CREDITS
def main() :

    print("This program finds the sum of the first n counting numbers")
    total_sum = 0
    count = 1

    num= eval((input("please input your n:")))
    while count <=num:
          total_sum = count + total_sum
          count =count +1
    print("the sum is" ,total_sum)

main()
