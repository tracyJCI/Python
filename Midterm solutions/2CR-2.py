def main():
    dracula = open('dracula.txt')
    text = dracula.read()
    dracula.close()

    # Keep everything up to and including "THE END"
    text = text[:text.find('THE END')+7]

    # Slowly whittle down the front matter of the book. First, keep only everything from 'CONTENTS' on. Then,
    # keep only everything from 'DRACULA' on. Finally, keep only everything from 'CHAPTER' on. Because we removed the
    # end matter earlier, we are now left with only the chapters and their text.
    text = text[text.find('CONTENTS'):]
    text = text[text.find('DRACULA'):]
    text = text[text.find('CHAPTER'):]

    # We will be working our way backwards from the last chapter, so set the chapter number to 27.
    chapter = 27

    while text:
        # Get the last chapter in the text and set chapter_text to anything from that point until the end of the text
        chapter_index = text.rfind('CHAPTER')
        chapter_text = text[chapter_index:]

        out = open('chapters/Dracula-Chapter-{}.txt'.format(str(chapter)), 'w')
        print(chapter_text, file=out)
        out.close()

        chapter -= 1

        # Since we're working backwards, keep everything up to the start of the current chapter
        text = text[:chapter_index]

main()
