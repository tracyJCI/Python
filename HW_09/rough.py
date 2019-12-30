import string
def main():
    filein = open("dracula.txt",'r')
    dracula = filein.read()
    chapters_beg = dracula.index("\n\n\n\nCHAPTER I")
    chapters_end = dracula.index(""" _There's More to Follow!_""")
    text = dracula[chapters_beg:chapters_end]
    new_list=[]
    for word in text.split():
        for punc in string.punctuation:
            word = word.replace(punc,"")
            word = word.lower()
        new_list.append(word)
    filein = open("stop_words.txt",'r')
    new_file = filein.read()
    stop_words = new_file.split(",")
    new_list2 = []
    for ac in new_list:
        if ac not in stop_words:
           new_list2.append(ac)
    dict ={}
    count = 0
    for ab in new_list2:
        for i in range(len(new_list2)):
            if ab == new_list2[i]:
               count = count+1
        if ab not in dict:
           dict[ab]= [count]

    print(dict)


main()
