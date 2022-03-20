# basics about python loops

import random

randomlist = random.sample(range(10, 30), 10)

print(randomlist)


search_engines_users = {
    "google": 1000000000,
    "bing": 127000000,
    "duck duck go": 12000000
}


# for engine in search_engines_users.items():
#     print(engine[1])

# for engine in search_engines_users.values():
#     print(engine)

    
# for engine in search_engines_users.keys():
#     print(engine)


index_list = 0

while index_list < len(randomlist):
    item = randomlist[index_list]
    if item % 2 == 1: 
        print(item)
    index_list += 1
