#KJC4 4CREDITS
def main():
    s1 = "spam"
    s2 = "ni!"
    caps = (s2.strip("!")).upper()#a
    print(caps)
    print(s2+s1+s2)#b
    repeat=(s1.capitalize()+" " + s2.capitalize()+ " ")*3 #c
    print(repeat)
    print(s1)#d
    myList = [s1[:2],s1[3]]#e
    print(myList)
    remove = s1[:2]+ s1[3]#f
    print(remove)


main()
