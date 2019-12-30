#PE13
#KJC4 4 CREDITS
def main():
   total_sum = 0
   amt=eval(input("How many numbers would you like to sum:"))
   for num in range(amt):
      num1 = eval(input("please input a number:"))
      total_sum = num1 + total_sum
   print("the sum is ", total_sum)

main()
