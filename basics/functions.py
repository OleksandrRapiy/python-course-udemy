def mean(list_data):
    if type(list_data) is dict and isinstance(list_data, dict):
        return sum(list_data.values()) / len(list_data)
    else:
        return sum(list_data) / len(list_data)


def mean_of_list(data):
    return sum(data) / len(data)


def mean_of_dict(dict):
    return sum(dict.values()) / len(dict)


data = list(range(1, 10))
dict_data = {
    "google": 1000000000,
    "bing": 127000000,
    "duck duck go": 12000000
}

mean_item = mean(data)
index_of_mean = data.index(mean_item)

print(mean_item)
print(index_of_mean)


print(mean(dict_data))

print(mean_of_dict(dict_data))


def is_value_in_list(x, list):
    return x in list

print(is_value_in_list(9, data))