 # zip code
'''
def validate(zipp_code):
    if len(zipp_code)==5 and zipp_code.isdigit():
        print("your zip code is accepted.")
    else:
        print("please provide a valid zip code(5 digits and all numbers)")

g=input("plesa insert your zip code: ")
validate(g)
'''

# black friday
'''
def products(products):
    price=0
    product = {
        "banana": 70000*0.93,
        "apple": 25000*0.95,
        "khiar": 12000*0.98,
        "carrot": 8000*0.9,
    }
    for item in products:
        price +=product[item]

    return print("your pay is",price,"tooman")
fruits=input("what fruits did you bought:").split()
products(fruits)
'''

# exception try
'''
def colculator(num1, operator, num2):
    if operator=="+":
        print("%d + %d ="%(num1, num2),num1+num2)
    elif operator=="-":
        print("%d - %d ="%(num1, num2),num1-num2)
    elif operator == "*":
        print("%d * %d ="%(num1, num2),num1*num2)
    elif operator== "/":
        print("%d / %d ="%(num1, num2),num1/num2)
    else:
        print("please insert a correct operator!")
try:
    num1=int(input("please give me a number to math operation:"))
    operator=input("please select an operator(+ - * /): ")
    num2=int(input("now provide second number to perform operation:")) 
except:
    print("something went wrong!")
else:
    colculator(num1, operator, num2)
'''

# extend lists
'''
samsung=["Galaxy A11", "Galaxy S23ultra", "Galaxy A23"]
apple=["Iphone11 pro", "Iphone10", "Iphone14"]
xiaomi=["redmi 1", "mi 12", "note 10"]

while(True):
    product=(input("please insert your product(press f to finish): "))
    if product=="f":
        break
    brand=input("mention the brand name(s for samsung, a for apple, x for xiaomi)")
    if brand == "s":
        samsung.append(product)
    elif brand == "a":
        apple.append(product)
    elif brand == "x":
        xiaomi.append(product)
    else:
        print("wrong symbol")
print("list of samsung products: ")
for i in samsung:
    print(i)
print("ـــــــــــــــــ")
print("list of apple products:")
for i in apple:
    print(i)
print("ـــــــــــــــــ")
print("list of xiaomi products:")
for i in xiaomi:
    print(i)
print("ـــــــــــــــــ")
print(samsung)

samsung.extend(apple)
allproducts=samsung
allproducts.extend(xiaomi)
for i in allproducts:
    print(i)
'''

# تکنیک برعکس کردن نوشته ها:
'''
x="hello"
print(x[::-1])
'''
# showing format
'''
def format_finder(namewithformat):
    first=namewithformat[len(namewithformat)-3:]
    print(first)

print(format_finder(input()))
'''
# security for card number
'''
def security_number(number):
    number = "**"*6+ number[-4:]
    print(number)
print(security_number(input()))
'''

# case sensivity
'''
def comparison(word1, word2, is_case_sensivity=False):
    word_1=word1.lower()
    word_2=word2.lower()
    if is_case_sensivity== True:
        return word1 == word2   
    else:
        return word_1==word_2
print(comparison("Ali", "ali", True))
'''

# password dondition
password=input("please provide a password(6 or 4 character and all number): ")
if ((len(password) == 6) and (password.isdigit()== True)) or ((len(password)==4) and (password.isdigit()==True)):
    print(True)
else:
    print(False)