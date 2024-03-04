def sed(input_file, output_file, pattern_string, replacement_string):
    try:
        with open(input_file, 'r') as input_f:
            with open(output_file, 'w') as output_f:
                for line in input_f:
                    returned_line = line.replace(pattern_string, replacement_string)
                    output_f.write(returned_line)

    except FileNotFoundError:
        print("Your file does not exist in your provided path")
        print("Please check the path and try again")
    except TypeError:
        print("The patterns has to be a string")
    else:
        print("The wanted output is ready now")


while True:
    try:
        input_file = input("Please enter input file path: ")
        output_file = input("Please enter output file path: ")
        pattern_string = input("Enter pattern string: ")
        replacement_string = input("And replacement string: ")
        sed(input_file, output_file, pattern_string, replacement_string)
        break
    except FileNotFoundError:
        print("Your file does not exist in your provided path")