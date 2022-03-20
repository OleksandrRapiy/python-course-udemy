FILE_PATH = 'files/supa_druppa.txt'

file =  open(FILE_PATH)

content = file.read()

file.close()

# we can open file and close without excplicit opening and closing (as using kword)
with open(FILE_PATH) as file: 
    file_content = file.read()

print(file_content)



# writing to file
with open(FILE_PATH, 'a') as file: 
    file.writelines(FILE_PATH)