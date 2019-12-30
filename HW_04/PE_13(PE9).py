# KJC4  4 CREDITS
def main():
    filein = open("phrases.txt", 'r')
    fileout= open("phrasesout2.txt", 'w')

    text= filein.read()
    text2 = text.split()
    print(len(text2), file= fileout)
    filein.close()
    fileout.close()
main()
