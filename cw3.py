import re


def increment_string(s):
    number = re.findall(r'\d+', s)
    if number:
        s_number = number[-1]
        print(s_number)
        s = s.rsplit(s_number, 1)[0]
        # s = re.split(r'\d+', s)[0]
        print(s)
        number = str(int(s_number) + 1)
        print(number)
        return s + '0' * (len(s_number) - len(number)) + number
    return s + '1'

increment_string('foo0243')