from operator import itemgetter

# init
n = int(input())
people = []
createOrder = {}
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age not in createOrder.keys():
        createOrder[age] = 1
    else:
        createOrder[age] += 1
    people.append({ 'age': age, 'order': createOrder[age] , 'name': name })

# sort
people = sorted(people, key=itemgetter('age', 'order')) 

# solve
for person in people:
    print(f"{person['age']} {person['name']}")