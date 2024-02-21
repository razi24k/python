# this function counts numbers contain 1, 2, or 3s and returns them with a particular syntax "dificulty: medium"
def look_and_say(word):
    result = ""
    onecntr = 0
    twocntr = 0
    thrcntr = 0
    for i in range(len(word)):
        if word[i] == "1":
            onecntr += 1
            if i+1 == len(word) or word[i] != word[i+1] :
                result += str(onecntr) + "1"
                onecntr = 0
        elif word[i] == "2":
            twocntr += 1
            if i+1 == len(word) or word[i] != word[i+1]:
                result += str(twocntr) + "2"
                twocntr = 0
        elif word[i] == "3":
            thrcntr += 1
            if i+1 == len(word) or word[i] != word[i+1]:
                result += str(thrcntr) + "3"
                thrcntr = 0
    return print(result)

look_and_say("221") # it contains two 2s and one 1 result: 2211
look_and_say("31131211131221") #result: 13211311123113112211