# netid : KJC4  4 CREDITS
def main():
 toc = """                      chapter VII

 Cutting from "The Dailygraph," 8 August                               71       """
 print("this demonstrates the lstrip method")
 st=toc.lstrip()
 print(st)
 print()

 print("this demonstrates the split method")
 sp=toc.split()
 print(sp)
 print()

 print("this demonstrates the join method")
 j=toc.join(["I", "am"," a", "lady"])
 print(j)
 print()

 print("this demonstrates the replace method")
 k=toc.replace("chapter","PAGE")
 print(k)
 print()

 word="mary,did you know"
 print("this demonstrates the capitalize method")
 l=word.capitalize()
 print(l)
 print()

 print("this demonstrates the center(width) method")
 m=word.center(30)
 print(m)
 print()

 print("this demonstrates the count method")
 n=word.count("you")
 print(n)
 print()

 print("this demonstrates the find method")
 n=word.find("you")
 print(n)
 print()

 new_word="AT"
 print("this demonstrates the left justify method")
 o=new_word.ljust(10)
 print(o)
 print()

 print("this demonstrates the lower method")
 p=new_word.lower()
 print(p)
 print()

 new_word_2="animal"
 print("this demonstrates the rfind method")
 q=new_word_2.rfind("a")
 print(q)
 print()

 print("this demonstrates the rjust method")
 r=new_word_2.rjust(15)
 print(r)
 print()

 new_word_3= "fabulous        "
 print("this demonstrates the rstrip method")
 s=new_word_3.rstrip()
 print(s,"ly")
 print()

 new_word_4= "rodents are horrible"
 print("this demonstrates the title method")
 t=new_word_4.title()
 print(t)
 print()

 print("this demonstrates the upper method")
 u=new_word_4.upper()
 print(u)
 print()


main()


