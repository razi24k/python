name=input('can you tell me your name? ')
def BMI (vazn, ghad):
    BMI=vazn/ghad**2
    return BMI
h=int(input("how much do you weigh?"))
g=float(input("what is your height?"))

if BMI(vazn=h, ghad=g)<=16.5:
    print("you're soooo thin",name)
elif 16.5<BMI(vazn=h, ghad=g)<=18.5:
    print("you're thin",name)
elif 18.5<BMI(vazn=h, ghad=g)<=25:
    print("you are healthly", name)
elif 25<BMI(vazn=h, ghad=g)<=30:
    print("you are fat a bit",name)
elif 30<BMI(vazn=h, ghad=g)<35:
    print("you're fat in degree 1",name)
elif 35<BMI(vazn=h, ghad=g)<40:
    print("you're fat in degree 2", name)
else:
    print("you are fat in degree 3 ",name,":OOOOO")