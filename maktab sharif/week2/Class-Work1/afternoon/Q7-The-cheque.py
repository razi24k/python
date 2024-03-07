the_number = input("Enter a number: ")
while the_number.isdigit() == False:
    print("Please enter a number. come on!")
    the_number = input("Enter a number: ")

my_dict0_9 = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

my_dict10_19 = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety'
}

if len(the_number) == 2:
if len(the_number) == 3 and the_number[1:] in my_dict10_19.keys():
    print(f"{my_dict0_9[the_number[0]]} hundred {my_dict10_19[the_number[-2:]]}")

