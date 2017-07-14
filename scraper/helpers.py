import re
from itertools import filterfalse

def remove_tags(input_string):
    res = re.search(r'<p>(.*)<', input_string)
    if res:
        input_string = res.group(1)
        if input_string.find("In ") is not -1:
            input_string = input_string.replace("In ", "")

    return input_string

    # for i in range(0, len(input_array)):
    #     res = re.search(r'<p>(.*)<', input_array[i])
    #     input_array[i] = res.group(1)
    #     if input_array[i].find("In ") is not -1:
    #         input_array[i] = input_array[i].replace("In ", "")

    # return input_array

def remove_extra(input_array):
    extracted = filterfalse((lambda x: len(x) > 30), input_array)
    return extracted