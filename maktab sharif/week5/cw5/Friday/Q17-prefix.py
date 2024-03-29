text = '''Python is an interpreted, object-oriented, high-level programming language
that can be used for a wide variety of applications. Python is a powerful
general-purpose programming language.'''
text_list = text.split("\n")

prefixed_text = ["* " + i for i in text_list]
for i in prefixed_text:
    print(i)
