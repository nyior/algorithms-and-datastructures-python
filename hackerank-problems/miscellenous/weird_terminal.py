"""
    Problem Statement – Here is a weird problem in Susan’s terminal. 
    He can not write more than two words each line, if she writes more than two, 
    it takes only 2 words and the rest are not taken. So she needs to use enter and
    put the rest in a new line. 
    For a given paragraph, how many lines are needed to be written in Susan’s terminal?

    input: a sentence
    key operation: how many lines in the terminal would the sentence require. Provided a line can
    take at most two words

    expected output: an integer representing the number of lines.

    steps 
    1. Get number of words in the sentence
    2. if words_count > num_lines = num_words//2 + num_words%2
    2
    3. return num_lines

    sample inputs: 0
    2
    3
    4
    5
    19

"""

def wierd_terminal(paragraph):
    words_count = len(paragraph.split(' '))

    if words_count >= 1:
        lines = (words_count//2) + (words_count%2)
        return lines
    else:
        return 0