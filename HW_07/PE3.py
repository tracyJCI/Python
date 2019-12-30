#KJC4 CREDITS
def main():
   points = float(input("please input the exam score:"))
   if points <= 100 and points >= 90:
      print(points ,"= A")
   elif points< 90 and points >= 80:
      print (points, "= B")
   elif points<80 and points >=70:
       print(points, "= C")
   elif points <70 and points >=60 :
       print(points, "= D")
   elif points <60:
       print(points,"F")

main()
