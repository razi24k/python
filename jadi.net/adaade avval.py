
def is_prime(n):
    aval= True
    for i in range(2,n):
        if n % i ==0:
            aval=False
    return aval

print("I want to tell you how many prime number is there in a certain range")
x=int(input("so tell me first number that you want:"))
y=int(input("OK! now tell me another number more than first:"))
while y < x:
    print("please enter a number bigger than first number, your first number was",x)
    y=int(input("OK! now tell me another number more than first:"))

prime_count= 0
for b in range(x,y+1):
    if is_prime(b):
        print(b, "adade avval")
        prime_count +=1

print("we had", prime_count,"prime number in this range")
