name=input("what's your name?")
tedade_nemoone_kaar=int(input('che tedad nemoone kar darid?'))
sabeghe_kaar=int(input('chand saal sabeghe kaar darid?'))
sen=int(input("chand saal darid?"))
eitiad=input("aya eitiad be har noa made mokhader darid? (y/n)")
if eitiad=='y':
    eitiad=True
elif eitiad=='n':
    eitiad=False

if (sen>=18 and not(eitiad)) or (sen>=40 and sabeghe_kaar>=20) or (sen>=18 and tedade_nemoone_kaar>=10) or (sabeghe_kaar>=5 and not(eitiad)):
    print('shoma estekhdam hastid',name)
else:
    print('moteasefam',name, 'shoma estekhdaam nashodid')