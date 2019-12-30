#KJC4 4CREDITS
def main():

    sum = 0
    num = eval(input("please input a number:"))
    sum = sum + num
    while num!= 999:

          num = eval(input("please input next number:"))
          if num == 999:
             break
          else :
               sum = sum + num
               print ("sum is" ,sum)
main()
