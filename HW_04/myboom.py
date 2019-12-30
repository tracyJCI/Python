filein = open('boomboom.txt', 'r')
fileout = open('boomboommiddle.txt', 'w')
#
text = filein.read()
#print(text)
#
beginning = text.find('''And Q R S! And T U V! Still more - W! And X Y Z!''')
end = text.find('''A is out of bed, and this is what he said, "Dare double dare, you can't catch me.''')
#
print(text[beginning:end])
