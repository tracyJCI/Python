import string


def main():
    out = open('counts.csv', 'w')

    headings = ','.join(['chapter', 'characters', 'words', 'lines'])
    print(headings, file=out)

    dracula = open('dracula.txt', 'r')
    text = dracula.read()
    dracula.close()

    contents_index = text.find('CONTENTS')
    dracula_index = text.find('DRACULA', contents_index)
    first_chapter_index = text.find('CHAPTER', dracula_index)
    end_index = text.find('THE END')

    body_text = text[first_chapter_index:end_index]

    for chapter_num, chapter in enumerate(body_text.split('CHAPTER')[1:]):
        chapter = 'CHAPTER' + chapter
        chapter = chapter.strip()  # remove extra whitespace to get the correct line count

        # We split on newlines and white space for the number of lines and words respectively. We simply get the length
        # of the entire chapter having replaced punctuation and white space for the letters variable.
        num_lines = len(chapter.split('\n'))
        num_words = len(chapter.split())
        num_characters = len(chapter)

        # Write the row with the chapter name to the output file and we're done! Notice we have to explicitly make the
        # numbers strings with str() since join() expects only string items.
        row = ','.join([str(chapter_num+1), str(num_characters), str(num_words), str(num_lines)])
        print(row, file=out)

    out.close()

main()
