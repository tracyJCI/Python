#KJC4 4CREDITS
def main() :
    filein = open("dracula.txt",'r')
    dracula = filein.read()
    beg = dracula.index("CONTENTS")
    end = dracula.index("\nDRACULA")
    table_of_contents = dracula[beg:end]
    mylist = table_of_contents.split("\n")
    for element in mylist:
        if element != "":
            if element.endswith("0")or element.endswith("1")or element.endswith("2")or element.endswith("3")or element.endswith("4")or element.endswith("5")or element.endswith("6")or element.endswith("7")or element.endswith("8")or element.endswith("9"):
               print(element)
    print("\nthe lines above are the lines in the dracula table of contents that have text and end with digits")

    filein.close()

main()
