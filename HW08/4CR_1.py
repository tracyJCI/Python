#KJC4 4CREDITS
def main():
    filein = open("dracula.txt",'r')
    count = 0
    while count <10:
          dracula=filein.readline()
          print(dracula)
          count= count+1
    print("These are the first", count," lines of the dracula file")
    filein.close()

main()
