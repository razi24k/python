import random
import matplotlib.pyplot as plt

random.seed()

people = [100 for i in range(50)]

for beshkan in range(100000):
    for person1 in range(len(people)):
        person2 = random.randint(0, 49)
        while people[person2] == 0:
            person2 = random.randint(0, 49)
        if people[person1] != 0:
            people[person1] = people[person1] - 1
            people[person2] = people[person2] + 1
people.sort()
plt.bar(range(0, 50), people)
plt.show()