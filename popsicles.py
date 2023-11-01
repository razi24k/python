def give_or_not(sib, pops):
    left_over=pops % sib
    if left_over ==0:
        print("give away")
    else:
        print("you have to eat %o popsicles in aloneless" %(left_over))
siblings=int(input("how many are brothers and sisters? "))
popsicles=int(input("how many is popsicles? "))
give_or_not(siblings,popsicles)

