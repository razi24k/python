fruits=["apple", "banana", "melon", "watermelon", "pineapple"]
vegetables=["carrot","tomato","onion","potato"]
fruits[1]="orange"
print(fruits[0:3])
fruits.insert(4,"banana")
print(fruits)
fruits.append("kiwi")

#**add two list:
fruits.extend(vegetables)

#**remove from lists
fruits.remove("carrot")
#or
fruits.pop(1)
del fruits[2]
#to delete list we use:            del fruits
#to delete members of list we use: fuits.clear()
fruits[8:11]="carrot", "orange", "watermelon"


1
"""
#1 Loop in lists

#1-1 For loop
for x in fruits:
    print(x)

#1-2 While loop
i=0
while i< len(fruits):
    print(fruits[i])
    i += 1

#1-3 Comprehension loop
[print(x) for x in fruits]
"""

2
'''
#2 comprehension lists
#2-1 without comprehension
witho=[]
for x in fruits:
    if "o" in x:
        witho.append(x)
print(witho)

#2-2 with comperhension
withm=[x for x in fruits if "m" in x]
print(withm)
#or
withoutapple=[x for x in fruits if x !="apple"]
print(withoutapple)
#or even
g_p=[x for x in range(4,15) if x < 10]
print(g_p)

#2-3 expression list
newlist=[x.capitalize() for x in fruits]
print(newlist)
#or
woutban=[x if x !="Banana" else "Khiaar" for x in newlist]
print(woutban)
'''


3
'''
#** sort lists
fruits.sort()
fruits.sort(reverse=True)

numbers=[70, 40, 87, 47, 105, 263, 1]
numbers.sort()
def myfunc(n):
    return abs(n-50)
numbers.sort(key=myfunc)
print(numbers)

fruits.sort(key=str.lower)
'''


4
'''
#** copy lists
the_list=list(fruits)
#or
List=fruits.copy()
'''


5
'''
#** join lists
thelist=[10,70,25,85]

for x in fruits:
    thelist.append(x)

#or
list3= thelist + fruits

#or
thelist.extend(fruits)
'''