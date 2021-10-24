name = input('Please inter your name?')
print('Hello')
print(name)

product = 'Suger'
category = 'Food'
cost = 2.0

print('this ' + product.capitalize() + ' is a ' + category.capitalize() + ' and it costs: ' + str(cost))

output = 'This is a {} and it is a {} and it is costs: {}'.format(product,category, cost)
print(output)

output_1 = 'This is a {0} and it is a {1} and it is costs: {2}'.format(product,category, cost)
print(output_1)

output_2 = f'This is a {product} and it is a {category} and it is costs: {cost}'
print(output_2)

# You can use functions to modify strings 
sentence = 'this dog is named sammy'
print(sentence.lower())
print(sentence.upper())
print(sentence.capitalize())
print(sentence.count('m'))

