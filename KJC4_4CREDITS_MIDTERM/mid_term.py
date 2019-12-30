#KJC4 4CREDITS
#MID TERM DRACULA PROCESSING PY FILE
def main():

    filein = open('dracula.txt','r')
    dracula = filein.read()
    chapters_beg = dracula.index("\n\n\n\nCHAPTER I")
    chapters_end = dracula.index(""" _There's More to Follow!_""")
    text = dracula[chapters_beg:chapters_end]
    split_text=text.split("\n\n\n\n\n")
    split_text[26] = split_text[26]+split_text[27]
    del(split_text[27])
    count = 1
    filein.close()

    filein = open("dracula.txt",'r')
    dracula2 = filein.read()
    beg = dracula2.index("CONTENTS")
    end = dracula2.index("\nDRACULA")
    table_of_contents = dracula2[beg:end]
    first_list = table_of_contents.split("\n")
    second_list = []
    third_list =[]
    for element in first_list:
        if element != "":
            if element.endswith("0")or element.endswith("1")or element.endswith("2")or element.endswith("3")or element.endswith("4")or element.endswith("5")or element.endswith("6")or element.endswith("7")or element.endswith("8")or element.endswith("9"):
               new_element = element[:-3]
               new_element2 = new_element.rstrip()
               second_list.append(new_element2)

    for element in second_list :
        quote=element.replace("'","")
        comma= quote.replace(",","")
        double_dash= comma.replace("--","")
        double_quote = double_dash.replace('"',"")
        space = double_quote.replace(" ", "_")
        period = space.replace(".","_")
        third_list.append(period)


    for chapter in split_text:
        filename = "Dracula-"+ "Chapter-" + str(count) +"-" +third_list[count-1] + ".txt"
        fileout = open(filename, 'w')
        print(chapter, file= fileout)
        fileout.close()
        count = count + 1
    filein.close()


main()

