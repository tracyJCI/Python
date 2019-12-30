#KJC4 4CREDITS
import string
def byFreq(pair):
    return pair[1]
def main():
    filein = open("dracula.txt",'r')
    dracula = filein.read()
    chapters_beg = dracula.index("\n\n\n\nCHAPTER I")
    chapters_end = dracula.index(""" _There's More to Follow!_""")
    text = dracula[chapters_beg:chapters_end]
    stripped_punc=[]
    
    for word in text.split():
        for punc in string.punctuation:
            word = word.replace(punc,"")
            word= word.lower()
        stripped_punc.append(word)
    filein = open("stop_words.txt",'r')
    new_file = filein.read()
    stop_words = new_file.split(",")
    stripped_stops = []
    
    for word in stripped_punc:
        if word not in stop_words:
           stripped_stops.append(word)
    dict ={}
    for new_word in stripped_stops:
        if new_word in dict:
           dict[new_word]= dict[new_word]+1
        else:
           dict[new_word]= 1
    items = list(dict.items())
    items.sort()
    items.sort(key=byFreq,reverse = True)
    
    for i in range(100):
        words,count = items[i]
        print("{0:<15}{1:>5}".format(words,count))



main()
