sample_data = [{"V": "S001"},
               {"V": "S002"},
               {"VI": "S001"},
               {"VI": "S005"},
               {"VII": "S005"},
               {"V": "S009"},
               {"VIII": "S007"}]

unique_values = []
for i in sample_data:
    for k, v in i.items():
        unique_values.append(v)
print(set(unique_values))