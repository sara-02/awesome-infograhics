import re

with open('text.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = sorted(lines)

# number
digit_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
              5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'ten',
              10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
              14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
              18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
              40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
              80: 'eighty', 90: 'ninety'}

transformed_lines = []
# print lines
for line in lines:
    print line
    if not re.findall(r"\[[0-9]+\b", line) == []:
        num = number = int(re.findall(r"\[[0-9]+\b", line)[0][1:])
        print number
        number_text = ''
        while number > 0:
            if number > 19 and number < 100:
                if (number % 10) > 0:
                    number_text = digit_word[(number % 10)] + ' ' + number_text
                else:
                    number_text = digit_word[number] + ' ' + number_text
                    number = 0
                number = number - (number % 10)

            elif number <= 19:
                number_text = digit_word[number]
                number = 0

            else:
                number_text = str(number)
                number = 0
        line = re.sub(str(num), number_text, line)
        print line
        transformed_lines.append(line)
    else:
        transformed_lines.append(line)

lines = sorted(transformed_lines)
with open('numtoword.txt', 'w') as f:
    f.write('\n'.join(lines))
