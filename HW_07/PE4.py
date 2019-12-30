#KJC4 4CREDITS
def main():
    credits =float(input("how many credits has student earned since enrolment:"))
    if credits < 7 :
        print("This student is a FRESHMAN")
    elif credits >= 7 and credits< 16 :
        print("This student is a SOPHOMORE")
    elif credits >= 16 and credits <26 :
        print("This student is a JUNIOR")
    elif credits >=26:
        print ("This student is a SENIOR")

main()
