nicknames = ["Haji", "Karbalaee", "Mashti"]

reg = input()
for i in range(len(reg)):
    if reg[i] == "Y":
        print(nicknames[i])
        break
    elif "Y" not in reg:
        print("Agha")
