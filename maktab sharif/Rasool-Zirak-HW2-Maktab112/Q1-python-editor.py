import os


def write_notes():
    try:
        # os.environ["TERM"] = "xterm"
        f = open("output.txt", "a")
        while True:
            user_input = input("Please enter your text here: ")
            f.write(user_input + "\n")
    except KeyboardInterrupt:
        os.system("clear")
        user_decision = input("\nplease enter 1 to continue\n2 to clear file\nand 0 to close\nenter here: ")
        while user_decision not in ["1", "2", "0"]:
            print("Invalid input.")
            user_decision = input("\nplease enter 1 to continue\n2 to clear file\nand 0 to close\nenter here: ")
        if user_decision == "1":
            write_notes()
        elif user_decision == "2":
            os.system("clear")
            print("with this choice all of contents will be cleared")
            authenticate = input("Are you sure?(y/n)")
            while authenticate not in ["y", "n"]:
                os.system("clear")
                print("Invalid input.")
                print("please enter y or n")
                authenticate = input("Are you sure?(y/n)")
            else:
                if authenticate == "y":
                    f.truncate(0)
                    os.system("clear")
                    print("File contents has been cleared.")
                    write_notes()
                elif authenticate == "n":
                    os.system("clear")
                    print("so let's continue")
                    write_notes()
        elif user_decision == "0":
            quitting = "n"
            quitting = input("Are you sure you want to quit?(y/n): ")
            while quitting not in ["y", "n"]:
                os.system("clear")
                print("Invalid input.\nplease enter y or n")
                quitting = input("Are you sure? ")
            if quitting == "y":
                f.close()
                return
            elif quitting == "n":
                os.system("clear")
                print("so let's continue")
                write_notes()
    finally:
        f.close()


write_notes()
