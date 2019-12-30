def main():
    filein = open('dracula.txt','r')
    dracula = filein.read()
    chapters_beg = dracula.index("\n\n\n\nCHAPTER I")
    chapters_end = dracula.index(""" _There's More to Follow!_""")
    text = dracula[chapters_beg:chapters_end]

    new_text= text.replace("\n\n\n", "%")
    

    for i in range(27):
        if i == 0:
           start = new_text.index("\nCHAPTER I")
           end = new_text.index("\nCHAPTER II")
           fileout=open("Dracula_Chapter_1.txt",'w')
           print(new_text[start:end], file= fileout)
        elif i==1:
            start = new_text.index("\nCHAPTER II")
            end = new_text.index("\nCHAPTER III")
            fileout = open("Dracula_Chapter_2.txt",'w')
            print(new_text[start:end], file=fileout)
        elif i ==2:
            start = new_text.index("\nCHAPTER III")
            end = new_text.index("\nCHAPTER IV")
            fileout = open("Dracula_Chapter_3.txt",'w')
            print(new_text[start:end], file = fileout)
        elif i == 3:
             start = new_text.index("\nCHAPTER IV")
             end = new_text.index("\nCHAPTER V")
             fileout = open("Dracula_Chapter_4.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i == 4:
             start = new_text.index("\nCHAPTER V")
             end = new_text.index("\nCHAPTER VI")
             fileout = open("Dracula_Chapter_5.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i == 5:
             start = new_text.index("\nCHAPTER VI")
             end = new_text.index("\nCHAPTER VII")
             fileout = open("Dracula_Chapter_6.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==6 :
             start = new_text.index("\nCHAPTER VII")
             end = new_text.index("\nCHAPTER VIII")
             fileout = open("Dracula_Chapter_7.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==7 :
             start = new_text.index("\nCHAPTER VII")
             end = new_text.index("\nCHAPTER VIII")
             fileout = open("Dracula_Chapter_8.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==8 :
             start = new_text.index("\nCHAPTER VIII")
             end = new_text.index("\nCHAPTER IX")
             fileout = open("Dracula_Chapter_9.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==9 :
             start = new_text.index("\nCHAPTER IX")
             end = new_text.index("\nCHAPTER X")
             fileout = open("Dracula_Chapter_10.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==10 :
             start = new_text.index("\nCHAPTER X")
             end = new_text.index("\nCHAPTER XI")
             fileout = open("Dracula_Chapter_11.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==11 :
             start = new_text.index("\nCHAPTER XII")
             end = new_text.index("\nCHAPTER XIII")
             fileout = open("Dracula_Chapter_12.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==12 :
             start = new_text.index("\nCHAPTER XIII")
             end = new_text.index("\nCHAPTER XIV")
             fileout = open("Dracula_Chapter_13.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==13 :
             start = new_text.index("\nCHAPTER XIV")
             end = new_text.index("\nCHAPTER XV")
             fileout = open("Dracula_Chapter_14.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==14 :
             start = new_text.index("\nCHAPTER XV")
             end = new_text.index("\nCHAPTER XVI")
             fileout = open("Dracula_Chapter_15.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==15 :
             start = new_text.index("\nCHAPTER XVI")
             end = new_text.index("\nCHAPTER XVII")
             fileout = open("Dracula_Chapter_16.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==16 :
             start = new_text.index("\nCHAPTER XVII")
             end = new_text.index("\nCHAPTER XVIII")
             fileout = open("Dracula_Chapter_17.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==17 :
             start = new_text.index("\nCHAPTER XVIII")
             end = new_text.index("\nCHAPTER XIX")
             fileout = open("Dracula_Chapter_18.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==18 :
             start = new_text.index("\nCHAPTER XIX")
             end = new_text.index("\nCHAPTER XX")
             fileout = open("Dracula_Chapter_19.txt",'w')
             print(new_text[start:end], file=fileout)
        elif i==19 :
             start = new_text.index("\nCHAPTER XX")
             end = new_text.index("\nCHAPTER XXI")
             fileout = open("Dracula_Chapter_20.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==20 :
             start = new_text.index("\nCHAPTER XXI")
             end = new_text.index("\nCHAPTER XXII")
             fileout = open("Dracula_Chapter_21.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==21 :
             start = new_text.index("\nCHAPTER XXII")
             end = new_text.index("\nCHAPTER XXIII")
             fileout = open("Dracula_Chapter_22.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==22 :
             start = new_text.index("\nCHAPTER XXIII")
             end = new_text.index("\nCHAPTER XXIV")
             fileout = open("Dracula_Chapter_23.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==23 :
             start = new_text.index("\nCHAPTER XXIV")
             end = new_text.index("\nCHAPTER XXV")
             fileout = open("Dracula_Chapter_24.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==24 :
             start = new_text.index("\nCHAPTER XXV")
             end = new_text.index("\nCHAPTER XXVI")
             fileout = open("Dracula_Chapter_25.txt",'w')
             print(new_text[start:end],file=fileout)
        elif i==25 :
             start = new_text.index("\nCHAPTER XXVI")
             end = new_text.index("\nCHAPTER XXVII")
             fileout = open("Dracula_Chapter_26.txt",'w')
             print(new_text[start:end],file=fileout)
        else :
             start = new_text.index("\nCHAPTER XXVII")
             end = new_text.index("""THE END""")
             fileout = open("Dracula_Chapter_27.txt",'w')
             print(new_text[start:end],file=fileout)

    filein.close()

     

main()
