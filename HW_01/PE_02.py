# NETID: KJC4  4 CREDITS
# PE2
# avg.py
# a simple program to average three exam scores
#  illustrates use of multiple input
def main ():
    print("this program computes the average of three exam scores.") #changed two to three
    score1, score2, score3 = eval(input("enter three scores seperated by a comma:"))# changed two to three and added score3
    average = (score1 + score2+ score3)/3  # changed denominator from 2 to 3 to have it compute for 3 scores
    print ( " the average of the scores is:", average)

main()



