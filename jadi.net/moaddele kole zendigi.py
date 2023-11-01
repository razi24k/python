n=int(input('moadele khod ra az sale avvale tahsil ta saale aakhar ra begoo:'))
moaddelha=0
teedad=0
while n!=10:
    print(n)
    n=int(input('moadele khod ra az sale avvale tahsil ta saale aakhar ra begoo:'))
    moaddelha=n+moaddelha
    teedad=teedad+1
    if n==10:
        moadele_kol=moaddelha/teedad
        print("moaddele tamaame salhaye tahsile shoma in meghdaar ast:", moadele_kol)
        
        