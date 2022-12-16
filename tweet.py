import re

neg = open('negative.txt', encoding="utf8")
with open('neg.txt', 'w') as negdata:
    for line in neg:
        new_string = " "
        lines = line.split("\n")
        for line2 in lines:
            values = line2.split(",")
            for value in values[2:]:
                new_string += value
            new_string = re.sub(r'\s+', ' ', new_string).strip()
            new_string = re.sub(r'@\w+', '', new_string)
            new_string = re.sub(r'[^\w\s]', '', new_string)
            new_string = new_string.lower()
            words = new_string.split(' ')
        negdata.write(','.join(words))
        negdata.write('\n')
            
pos = open('positive.txt', encoding="utf8")
with open('pos.txt', 'w') as posdata:
    for line in pos:
        new_string = " "
        lines = line.split("\n")
        for line2 in lines:
            values = line2.split(",")
            for value in values[2:]:
                new_string += value
            new_string = re.sub(r'\s+', ' ', new_string).strip()
            new_string = re.sub(r'@\w+', '', new_string)
            new_string = re.sub(r'[^\w\s]', '', new_string)
            new_string = new_string.lower()
            words = new_string.split(' ')
        posdata.write(','.join(words))
        posdata.write('\n')
