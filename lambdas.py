# To understand lambdas let us try to see what problems it can solve?

# Let us sort some objects and each object has two proprties
presenter = [
    {'name':'Abdullah', 'age':'40'},
    {'name': 'Susan', 'age': '30'}
]
#presenter.sort()
#print(presenter)

# The presvious code will raise an error when you run, because it does not know wether to sort by name or by age 
# luckily there is a neat feature with sort
# sort can atuomatically handle primitive types and strings, If we need to do anything complex we need to tell sort how to sort.
# In this case we need to specify wether to sort by name or by age 
# So here, there is a key parameter that allows us to pass in a function that can grab or indexing whatever we want form a list or dic.

def indexing_func(item):
    return item['name'] 

presenter.sort(key= indexing_func)
print(presenter)

# In our previous case we sepcified a little function to determine which element we need to sort by and here we need to sort by name.
# as we determined in the indexing_func


# But here there is a solution using lambdas function, so we don`t need to declare an explicit function, so using lambdas we can done it 
# just inline in your code. SO we can just say 
presenter.sort(key= lambda item: item['name'])
print(presenter)
# As we declare the function lambdas inside the parameter key, we specified the item as a parameter of the lambda and the value that we 
# want to be returned it is the name.

# You can also sort the results by the length of the name
presenter.sort(key= lambda item: len(item['name']))
print(presenter)




