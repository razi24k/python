# This function returns all Continuous vowels that repeated more than one time "dificulty: medium"
def find_repeated(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    returned_list = []
    vowels_counter = 0
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_counter += 1
        else:
            if vowels_counter > 1:
                returned_list.append(word[i-vowels_counter:i])
            vowels_counter = 0
            
    return returned_list
print(find_repeated("rabcdeefgyYhFjkIoomnpOeorteeeeet")) # result: ['ee', 'Ioo', 'Oeo', 'eeeee']