import os

# control variables
total = 0
deleted = 0

# iterate over every file in given directory
for file in os.listdir("italian_sounds"):
    total += 1
    if file[-4:] != ".wav":
        deleted += 1
        #os.remove("italian_sounds/{}".format(file))

print("Total files: {}".format(total))
print("Deleted files: {}".format(deleted))
print("Files left: {}".format(total - deleted))