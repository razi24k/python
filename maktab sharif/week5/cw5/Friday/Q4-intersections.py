A = {'Tamil': 92, 'English': 56, 'Maths': 88, 'Sceince': 97, 'Social': 89, "Sina": 20}
B = {'Tamil': 78, 'English': 68, 'Maths': 88, 'Sceince': 97, 'Social': 56, "Reza": 20}

for key, value in A.items():
    for k, v in B.items():
        if value == v and key == k:
            print(f"{k}: {v} is present in Both A and B")