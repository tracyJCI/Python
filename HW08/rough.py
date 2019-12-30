def main():
    filein = open("dracula.txt",'r')
    dracula = filein.read()
    beg = dracula.index("CONTENTS")
    end = dracula.index("\nDRACULA")
    table_of_contents = dracula[beg:end]
    mylist = table_of_contents.split("\n")
    count = 0
    while count<2:
          for element in mylist:
               print(element)
               count = count + 1
    print("these are the first", count , "lines of the dracula table of content")
    filein.close()
main()
