from collections import namedtuple

Factory = namedtuple("Factory", "name, q1, q2, q3, q4, average")

FACTORY_COUNT = 4
factories = list()

for i in range(FACTORY_COUNT):
    name = input("Please, enter factory title\n")
    q1 = int(input("Please, enter revenue in the first quarter\n"))
    q2 = int(input("Please, enter revenue in the second quarter\n"))
    q3 = int(input("Please, enter revenue in the third quarter\n"))
    q4 = int(input("Please, enter revenue in the fourth quarter\n"))
    average = (q1 + q2 + q3 + q4) / 4
    factories.append(Factory(name, q1, q2, q3, q4, average))

average_revenue = 0
for i in range(FACTORY_COUNT):
    average_revenue += factories[i].average

average_revenue /= FACTORY_COUNT

print("Average revenue is:", average_revenue)
print("Factories with revenue above average:", [(x.name, x.average) for x in factories if x.average > average_revenue])
print("Factories with revenue below average:", [(x.name, x.average) for x in factories if x.average < average_revenue])
