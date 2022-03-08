search_engines_users = {
    "google": 1000000000,
    "bing": 127000000,
    "duck duck go": 12000000
}


print(search_engines_users.get("bing"))

print(search_engines_users['bing'])


# convert list to dictionary 
data = [['name','alex'], ['some', 'another']]

dict_data = dict(data)
print(dict_data)