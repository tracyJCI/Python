def main():
    #for ch in "aardvark":
       # print(ch)

    #for w in "Now is the winter of our discontent...".split():
        #print (w)
     #for w in "Mississippi".split("i"):
         #print(w,end="")

    #msg=""
    #for s in"secret".split("e"):
        #msg =msg+s
    #print(msg)
    msg = ""
    for ch in "secret":
        msg= msg + chr(ord(ch)+ 1)
    print(msg)

main()

