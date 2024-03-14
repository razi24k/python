import pprint
my_list = []
with open("note.txt", "r") as f:
    text_list = f.readlines()
    http_statuses = []
    http_method = []
    response_size = 0
    for i in text_list:
        x = i.split(" ")
        http_statuses.append(x[5][1:])
        http_method.append(x[8])
        if x[9][:-2].isdigit():
            response_size += int(x[9])
status_dict = dict()
method_dict = dict()
for i in set(http_statuses):
    status_dict[i] = http_statuses.count(i)
for i in set(http_method):
    method_dict[i] = http_method.count(i)

#         pprint.pprint(x1)
# print(f"total requests: {len(my_list)}")

print(f"total requests: {response_size}")
print(f"HTTP methods: {method_dict}")
print(f"HTTP statuses: {status_dict}")



# Q number Log :)
# import pprint
# file = open(file='note.txt', mode="r")
# lines_list = file.readlines()
# frequency_dict = dict()
# get = 0
# post = 0
# status200 = 0
# status302 = 0
# response_size = 0
# for word in lines_list:
#     if word[5][1:] == "GET":
#         frequency_dict["GET"] = get + 1
#     elif word[5][1:] == "POST":
#         frequency_dict["POST"] = post + 1
#     elif word[8] == "200":
#         status200 += 1
#     elif word[8] == "302":
#         status302 += 1
#
# pprint.pprint(lines_list)



# for word in set(main_list):
#     counter = main_list.count(word)
#     if counter >= 1:
#         frequency_dict.update({word: counter})
#
#
# print(f"""
#
# Total Requests: {frequency_dict.get('-')/2}
# HTTP Methods:
#   GET: {frequency_dict.get('"GET')}
#   POST: {frequency_dict.get('"POST')}
#   ...
# HTTP Status Codes:
#   200: {frequency_dict.get('200')}
#   302: {frequency_dict.get('302')}
#   304: {frequency_dict.get('304')}
#   ...
# Total Response Body Size:-
# """)
