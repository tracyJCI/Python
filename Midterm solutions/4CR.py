import string  # We will use the list of punctuation marks in the 'string' module later, so we have to import it here


def main():
    text = open('dracula.txt')
    lines = text.readlines()
    text.close()

    contents_index = lines.index('CONTENTS\n')
    dracula_index = lines.index('DRACULA\n')

    # We will keep track of chapter titles here
    chapters = []

    # Any line between 'CONTENTS' and 'DRACULA' is the TOC, so let's look only at these lines for now
    for line in lines[contents_index:dracula_index]:
        # Replace all punctuation in string.punctuation
        for mark in string.punctuation:
            line = line.replace(mark, '')

        line_words = line.split()

        # Having looked at the TOC, we can see that chapter lines have two words ("Chapter" and the number), "Page" is
        # one word, empty lines are length 0. Anything else is the chapter title (plus page numbers).
        if len(line_words) > 2:
            # Join words with underscores, but leave out the page number at index -1
            title = '_'.join(line_words[:-1])

            chapters.append(title)

    text_without_header = lines[dracula_index:]

    chapter = 0
    line_count = 0
    line = text_without_header[line_count]
    while 'THE END' not in line:
        if 'CHAPTER' in line:  # A chapter heading: increase the chapter count and open the chapter file
            chapter += 1
            out = open('chapters/Dracula-Chapter-{}-{}.txt'.format(str(chapter), chapters[chapter-1]), 'w')

        if chapter > 0:  # Only write if we have seen at least one chapter, i.e. ignore white space before 'CHAPTER I'
            out.write(line)

        line_count += 1
        line = text_without_header[line_count]


main()
