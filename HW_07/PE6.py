#KJC4 4CREDITS
def main():
    limit = float(input("please input the speed limit:"))
    speed = float(input("please input the clocked speed:"))
    if speed > limit and speed <=90 :
       over_mph = speed - limit
       fine = (over_mph*5)+ 50
       print("the fine is", fine,"$")
    elif speed > limit and speed >90:
         over_mph = speed-limit
         fine = ( over_mph * 5)+50+200
         print("the fine is", fine,"$")
    elif speed <= limit :
         print ("LEGAL SPEED")

main()
