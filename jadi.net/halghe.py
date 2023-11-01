def hala_yarom_bia(shoma, ma):
    ma=75
    ma_hame= shoma + ma
    ma = ma_hame-shoma
    shoma = ma_hame-ma
    
    return ma_hame
    
    
x=int(input("shoma chand nafarid?"))
print("ma ham 75 nafar hastim...")

print("midooni age ba ham bashim chand nafar mishim؟",hala_yarom_bia(shoma=x,ma=75),"ta")
   
