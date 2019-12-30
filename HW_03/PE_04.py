#KJC4  4 CREDITS
def main():
    phrase = input("please enter a phrase :")
    word = phrase.split()
    message = ""
    for i in range(len(word)):
        word_2=(word[i])
        word_3=(word_2[0]).split()
        message = message + word_3[0]
    print("the acronym of that phrase is " ,message.upper())
main()

