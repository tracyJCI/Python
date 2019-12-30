#PE14
#KJC4 4 CREDITS
def main():
   total_sum = 0
   amt=eval(input("How many numbers are there:"))
   for num in range(amt):
      num1 = eval(input("please input a number:"))
      total_sum = num1 + total_sum
      avg = total_sum/amt
   print("the average of the numbers is ", avg)

main()
