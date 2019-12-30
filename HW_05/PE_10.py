#KJC4 4CREDITS
def acronym(input_phrase):
    split_phrase = input_phrase.split()
    create_acronym=""
    for word in split_phrase:
        create_acronym = create_acronym + word[0]
    return(create_acronym.upper())



print("this program finds the acronym of any phrase you enter")
user_phrase = input("please enter a phrase :")
acronym_result = acronym(user_phrase)
print ("The acronym of your phrase is ", acronym_result)
