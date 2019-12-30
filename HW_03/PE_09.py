#KJC4 4 CREDITS
def main():
    word = input("please enter a sentence :")
    word_2 = word.split()
    counter = 0
    for ch in word_2:
        counter = counter + 1
    print("you have",counter, "words in your sentence")
main()
