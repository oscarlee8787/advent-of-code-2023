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
    turns every number words into numbers with a dictionary
    execute the same function from before
    '''
    # sample_list = text.splitlines()
    # for line in sample_list:
    #     if re.findall('one', line):
    #     # text.replace(a, 'HIIIII')
    #         print(f"found {line}")
    #         line.replace('one', 'HIIII')
    #         print(line)
    # # print(text.replace('two','HHHHHHH'))
    # print(text)

    text_list = text.splitlines()
    # for line in text_list:


    # for digits in num_dict.keys():
    #     # print(digits)
    #     text = text.replace(digits, str(num_dict[digits]))
    string = 'threeightwothreenine'
    pattern = r"one|two|three|four|five|six|seven|eight|nine"
    matched = list(re.finditer(pattern, string))

    print(f'first match: {matched[0].group(0)}')
    print(f'last match: {matched[-1].group(0)}')

    return

decode_str(sample)
