sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000, 
    "city": "New york"
}

# if "city" in sample_dict.keys():
#     sample_dict.update({"location" : sample_dict.get("city")})
#     del sample_dict["city"]
# print(sample_dict)

sample_dict['location'] = sample_dict['city']
del sample_dict['city']
print(sample_dict)
