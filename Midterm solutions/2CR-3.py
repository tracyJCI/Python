def main():
    # Read in the entire Dracula file as one big string.
    dracula = open('dracula.txt')
    text = dracula.read()
    dracula.close()

    contents_index = text.find('CONTENTS')
    dracula_index = text.find('DRACULA', contents_index)
    first_chapter_index = text.find('CHAPTER', dracula_index)
    end_index = text.find('THE END')

    body_text = text[first_chapter_index:end_index+7]

    chapters = body_text.split('CHAPTER')

    # When we split on chapter, it created an empty string as the first element, so we remove that
    del chapters[0]

    for i, chapter in enumerate(chapters):
        out = open('chapters/Dracula-Chapter-{}.txt'.format(str(i+1)), 'w')

        # Since splitting on 'CHAPTER' also removes the word, we have to insert it back in
        print('CHAPTER'+chapter, file=out)

        out.close()


main()
