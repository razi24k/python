x=int(input('masire shoma chand metr ast?'))
y=int(input('faseleye beine cheraghha chand metr baashad?'))

def kole_cheragh_ha(tool,fasele):
    tedade_cheragh=tool//fasele*2
    baghimande=tool%fasele
    tedade_tir=tool//fasele
    hazineha=(tedade_cheragh*50000)+(tedade_tir*300000)

    return 'tedade cherage morede niaz:',tedade_cheragh,'tedade tir barghe morede niaz:',tedade_tir,'hazineye kol:',hazineha,'tooman','baghi mande masir:',baghimande,

print(kole_cheragh_ha(tool=x,fasele=y))
edame=input("edame?(y/n)")
