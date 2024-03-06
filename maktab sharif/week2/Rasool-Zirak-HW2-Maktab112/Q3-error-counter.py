try:
    with open("source-code.py", "r") as source:
        errors = 0
        source_list = source.readlines()
        for i, line in enumerate(source_list):
            try:
                compile(line, "code", "exec")
            except SyntaxError:
                errors += 1
                print(f"Syntax error in line {i + 1}; number of errors: {errors}")
except FileNotFoundError:
    print("File not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")
