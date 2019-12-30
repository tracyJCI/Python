def main():
    text = open('dracula.txt')
    lines = text.readlines()
    text.close()

    dracula_index = lines.index('DRACULA\n')
    text_without_header = lines[dracula_index:]

    chapter = 0
    line_count = 0
    line = text_without_header[line_count]
    while 'THE END' not in line:
        if 'CHAPTER' in line:
            chapter += 1
            out = open('chapters/Dracula-Chapter-{}.txt'.format(str(chapter)), 'w')

        if chapter > 0:
            print(line, file=out, end='')

        line_count += 1
        line = text_without_header[line_count]

    # Write the "THE END" line
    print(line, file=out, end='')


main()
