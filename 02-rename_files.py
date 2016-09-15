import os

# open text file with file_name map and store into dictionary
with open("media.txt", "r") as file:
    name_map = eval(file.read())
# close file
file.close()

# iterate over dictionary
for key in name_map:
    os.rename("italian_media/{}".format(key), name_map[key])
    #print(key + ": " + name_map[key])