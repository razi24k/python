def sed(input_file, output_file, pattern_string, replacement_string):
    with open(input_file, 'r') as input_f:
        with open(output_file, 'w') as output_f:
            for line in input_f:
                returned_line = line.replace(pattern_string, replacement_string)
                output_f.write(returned_line)
    return output_f


while True:
    stop = input("press any key to continue and s to stop: ")
    if stop == "s":
        break
    try:
        in_file = input("Please enter input file path: ")
        out_file = input("Please enter output file path: ")
        pattern = input("Enter pattern string: ")
        replacement = input("And replacement string: ")
        sed(in_file, out_file, pattern, replacement)
        break
    except FileNotFoundError:
        print("Your file does not exist in your provided path")
