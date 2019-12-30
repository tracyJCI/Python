filein = open("smalltext.txt", "r ", encoding ='utf8')#i/o object
fileout = open('smalltextout.txt', 'w')
#step1  open the files and remember the names

#print(filein)
text = filein.read()
print(text.split())

filein.close()
filein = open('samlltext.txt', 'r')

for line in range(3):
    text = filein.readline()
    fixed = text.strip()
    print(fixed)

line1= filein.readline()
line2 = filein.readline()

print(line1.strip())
#step2 do something with the files
#[] - indicates a list
#'' indicates a string
#() indicates integers or floats- numbers

#step3 close all your files
filein.close() #manage memory space
fileout.close()


filein = open('smalltext.txt', 'r')
print(filein.readlines()) #splits but puts it into a list


filein = open ('boomboom.txt', 'r')
fileout = open ('boomboommiddle.txt', 'w')

text = filein.read() # read() makes it a string
print(text)
 alltext =[]

for line in range(10):
      text = filein.readline()
      alltext.append(text)


begiining = alltext.index('''huhgjhj\n''')
middle = alltext[6:16]
print(''.join(middle))


beginning = text.find('''kjhkhjk''')
end =  text.find('''kokok''')
print (text[beginning:end], file = fileout)

beginning= alltext.index('' '' '')
middle

filein.close()
fileout.close()
