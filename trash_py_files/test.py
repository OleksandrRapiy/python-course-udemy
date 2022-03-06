import random


# using of array
array_data = [1, 'some', 43.2, 's']

# for i in array_data: 
#     print(type(i))

# using of range
list_range = list(range(1, 10))
# print(list_range)


random_list = random.sample(range(10, 100), 5)

print(random_list)
print(min(random_list))


dictionary = {'some': 1, 'some2': 2, 'another': 5}

for item in dictionary:
    print(dictionary[item])

print(dictionary.values())

day_temperatures = {'morning':  (3.3,4.4, 42.3), 'noon': (3.3,4.4, 42.3), 'evening':  (3.3,4.4, 42.3) }

print(day_temperatures.values())