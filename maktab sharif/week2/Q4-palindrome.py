text = input("Enter a string: ").lower()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")