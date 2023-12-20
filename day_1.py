'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

'''

def decode(a):
    '''
    Goes through line by line, for each line, finds the first digit from the left and the first digit from the right,
    appends the two digits into a 2-digit number,
    add the number to a list,
    returns the sum of the list
    '''
    list_ = a.splitlines()
    num_list = []
    for ele in list_: # for every line in the whole text
        for i in ele:
            if i.isdigit():
                num = str(i) # go through every position starting from the left until the first digit is found
                break
        for j in reversed(ele):
            if j.isdigit():
                num2 = str(j) # go through every position starting from the right until the first digit is found
                break
        num_list.append(int(num.join(num2)))

    print(num_list)
    return num_list

text = '''1hhh2
1dff2'''

decode(text)
