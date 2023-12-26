'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

'''

import re

num_dict = {'one':1,
'two':2,
'three':3,
'four':4,
'five':5,
'six':6,
'seven':7,
'eight':8,
'nine':9}

list_ = ['one']

sample = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

def decode_str(text):
    '''
    turn text into list of strings
    use regex to find all instances of 'one' to 'nine'
    save found instances in a list
    replace first and last instance with numbers
    execute the same function from before
    '''

    text_list = text.splitlines()
    for line in text_list:
        pattern = r"one|two|three|four|five|six|seven|eight|nine"
        matches = list(re.finditer(pattern, line)) # for every line, find every instance that matches
        # one of the patterns starting from the beginning of the line
        for match in matches: # replace the words with numbers one by one
            line = line.replace(match.group(0), str(num_dict[match.group(0)]))
    print(line)

    num_list = []
    for ele in text_list: # for every line in the whole text
        for i in ele:
            if i.isdigit():
                num = str(i) # go through every position starting from the left until the first digit is found
                break
        for j in reversed(ele):
            if j.isdigit():
                num2 = str(j) # go through every position starting from the right until the first digit is found
                break
        num_list.append(int(num + num2))

    print(sum(num_list))

    return

decode_str(sample)
