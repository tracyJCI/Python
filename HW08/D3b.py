#KJC4 4CREDITS
def main() :

    print("This program finds the sum of the first n odd numbers")
    total_sum = 0
    count = 1

    num= eval((input("please input your n:")))
    while count <=(2*num)-1:
          total_sum = count + total_sum
          count =count +2
    print("the sum is" ,total_sum)

main()
