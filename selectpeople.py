#select random people to give a doller for 10000 times


import random
import matplotlib.pyplot as plt

random.seed()                                          #faster processing program
people = []                                            #define a array
for i in range(0, 50):
    people.append(100)

for beshkan in range(0, 10000):
    for person1 in range(0,50):
        person2 = random.randrange(0, 50)
        while people[person2] == 0:                    #if the second person hasn't doller, finishe program
            person2 = random.randrange(0, 50)
        if people[person1] != 0:                       #while the first person has doller
            people[person1] = people[person1] -1
            people[person2] = people[person2] +1

plt.bar(range(0,50), sorted(people,reverse=True))
#use sorted function to sort datas and use reverse to sorted left side

plt.show()

print(people)
#after 10000times, people have doller =====> print(people)
