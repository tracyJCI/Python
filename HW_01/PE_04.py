# net ID : KJC4 4 CREDITS
# PE4
#convert.py
# a program to convert celsius temps to fahrenheit
# by: susan Computewell


def main():
    print("the celsius temperatures and fahrenheit values are")
    celsius=[0,10,20,30,40,50,60,70,80,90,100]
    for x in range(11):
      fahrenheit = 9/5 * celsius[x] + 32
      print(celsius[x]," ",fahrenheit)
      print()



main()
