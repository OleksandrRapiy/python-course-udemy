string = 'this is some string'

print(string[-10:])

list_data = [string, 1, 'another string']

print(list_data[0][:6])



# string formating 
user_name = input('Enter your name: ')
message = 'Hello mr/ms %s!'%user_name
message2 = f'How is going {user_name}'

print(message)
print(message2)
