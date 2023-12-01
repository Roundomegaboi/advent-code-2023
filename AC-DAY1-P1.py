#advent of code day 1 part 1
info = open('day1.txt','r')

total = 0
for line in info.readlines():
    line = line.replace('\n','')
    digits = []
    for letter in line:
        if letter.isnumeric():
            digits.append(letter)
            
    first = digits[0]
    last = digits[len(digits)-1]
    
    number = int(str(first) + str(last))
    
    total += number
            
print(total)
info.close
