names={"Ali","Hasan", "Shayan","Mehrdad","Mohammad", "Kamran", "Abbas"}
families={"Haashemi", "Sarbaz", "Tavakoli", "Zand", "Asefi","Ali"}

##families.intersection_update(names)
##print(families)

##names.difference_update(families)
##print(names)

names.symmetric_difference_update(families)
print(names)