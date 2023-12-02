#advent of code day 1 part 2
info = open('day1.txt','r')


numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
    }


total = 0
for line in info.readlines():
    line = line.replace('\n','')
    digits = []
    string = ''
    for letter in line:
        if letter.isnumeric():
            digits.append(int(letter))
            string = ''

        else:
            string += letter
            for key in numbers:
                if key in string:
                    digits.append(numbers[key])
                    string = string[len(string)-1]


    first = digits[0]
    last = digits[len(digits)-1]

    number = int(str(first) + str(last))
    total += number
            
print(total)
info.close

