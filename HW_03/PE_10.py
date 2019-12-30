#KJC4 4 CREDITS
def main():
    word = input("please enter a sentence :")
    word_2 = word.split()
    counter = 0
    total_word_length = 0
    for ch in word_2:
        total_word_length = total_word_length + len(ch)
        counter = counter + 1
    avg_word_length = total_word_length/counter    
    print ("the total word length is",total_word_length)
    print("the number of words is ",counter)
    print("the average word length is:", avg_word_length)
main()
