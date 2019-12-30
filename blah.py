Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
import string
def main():
    filein = open("dracula.txt",'r')
    #dracula = filein.readlines()
    dracula = filein.read()
    #print(dracula)
    chapters_beg = dracula.index("\n\n\n\nCHAPTER I")
    chapters_end = dracula.index(""" _There's More to Follow!_""")
    text = dracula[chapters_beg:chapters_end]
    newlist=[]
    for word in text.split():
        for punc in string.punctuation:
            word=word.replace(punc,"")
            word= word.lower()
        newlist.append(word)
    #print(newlist)
    filein = open("stop_words.txt",'r')
    new_file = filein.read()
    stop_words = new_file.split(",")
    #print(stop_words)
    newlist2 = []
    for word in newlist:
        if word not in stop_words:
           newlist2.append(word)
    #print(newlist2)
    dict ={}
    count = 0
    i=0
    for word in newlist2:
        for i in range(129559):
            if word== newlist[i]:
               count = count+1
               i = i+1
        if word not in dict:
           dict[word]= count

    print(dict)

