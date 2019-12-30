# KJC4 4 CREDITS
def main():
    filein = open("dracula.txt", 'r')
    str = " "
    for line in range(15975):
        str2 = filein.readline()
        str = str + str2

    str3= str.split("\n\n")

    begin = str3.index("\nCONTENTS")
    end = str3.index("\nDRACULA")
    str4 = str3[begin:end]
    print(str4)

    filein.close()



main()
