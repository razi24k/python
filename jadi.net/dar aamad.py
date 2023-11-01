



def hoghooghe_yek_rooz(hour, income):

    daramade_to_dar_rooz= hour*income
   
    return daramade_to_dar_rooz
x=int(input("how many hours do you work in a day?:"))
y=int(input("how much does your boss pay for you for an hour?:"))
if x>=8 and y>=10:
    print("hmmm, you're such a sucsessful employee:)")
elif 8>x>=4 and 4<=y<10:
    print("you can work more and earn more money dear friend!")
elif 0<=x<4 and y<4:
    print("lazy guys can't have much money:(")
elif x<0:
    print("error! first question can't have a negative number.")
elif x>=8 and 8<=y<10:
    print("hmmm. it looks good")
elif x>=8 and y<8:
    print("why do you work for this boss?")
elif 8>x>=4 and y>=10:
    print("don't miss your job.")
elif 8>x>=4 and  y<4:
    print("I think you can find a better job if you look for it and work harder") 
elif 0<=x<4 and y>=10:
    print("interesting job. can you cennect us with your boss?!!!!!")
elif 0<=x<4 and 4<=y<10:
    print("It's a great job for a lazy guy like you.")
else:
    print('erorr! unexpected incident')


print("your income in a day is:",hoghooghe_yek_rooz(hour=x, income=y))