# KJC4 4 CREDITS
def main():
    filein = open('phrases.txt','r')
    fileout = open('phrasesout.txt','w')

    text= filein.read()
    text2= text.split()
    text3=""

    for word in text2:
        text3 = text3 + word[0]
    text4 = text3.upper()

    print (text4, file=fileout)
    filein.close()
    fileout.close()
main()
