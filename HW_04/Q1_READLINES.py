# KJC4 4 CREDITS
def main():
    filein = open('dracula.txt','r')
    text = filein.readlines()

    begin = text.index("CONTENTS\n")
    end = text.index("DRACULA\n")
    str = text[begin:end]
    print(str)

    filein.close()

main()
