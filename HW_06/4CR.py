#KJC4 4CREDITS
def main() :
    filein = open("dracula.txt",'r')
    dracula = filein.read()
    beg = dracula.index("CONTENTS")
    end = dracula.index("\nDRACULA")
    table_of_contents = dracula[beg:end]
    mylist = table_of_contents.split("\n")
    for element in mylist:
        if element[0:7] != "CHAPTER" and element != "":
           print(element)
    print("\nthe lines above are the lines in the dracula table of contents that have text and do not start with CHAPTER")

    filein.close()

main()
