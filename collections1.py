person_1 = {}
person_1['first'] = 'Ali'
person_1['last'] = 'Mo'

person_2 = {}
person_2['first'] = 'Susan'
person_2['last'] = 'Harrison'

people = []
people.append(person_1)
people.append(person_2)
people.append({
    'first': 'Bill', 'last': 'Gates'
})
print(people)