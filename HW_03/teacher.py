def main():
    phrase = input('Phrase to be acronymized: ')

    words = phrase.split()  # split phrase on white space to create a list of words

    first_letters = ''
    for word in words:
        first_letters = first_letters + word[0]  # add the first letter of each word

    print(first_letters.upper())


main()
