list_range = list(range(1, 10))

# type of indexing in python
# get all item from the start to the index 
print(list_range[:5])

# get all items bettwen index
print(list_range[2:5])

# get all items from index till the end
print(list_range[2:])

# get last item from the list using negative indexing 
print(list_range[-1])


print(list_range[-7:])


# list comprehension 

temps = [1223, 321, 543, 321, -421, 432, -432]

new_temps = [temp / 10 for temp in temps]

print(new_temps)


# list comprehension with condition 
new_temps_not_less_than_zero = [temp / 10 for temp in temps if temp > 0 ]



print(new_temps_not_less_than_zero)