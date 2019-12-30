# KJC4 4 CREDITS
def main():
    filein = open("dracula.txt", "r", encoding ='utf8')
    text = filein.read()
    text2 = text.split('\n\n')

    begin = text2.index("\nCONTENTS")
    end = text2.index("\nDRACULA")
    text3= text2[begin:end]
    print(text3)

    filein.close()



main()
