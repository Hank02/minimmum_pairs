# each sound has two things associated: filename and word
# each min_pair has two sounds, so each pair has four elements
# this script groups each min_pair into a 4-element list
# and stores that into a dictionary

# open files
oldfile = open("word_list.txt", "r")
newfile = open("pairs_list.txt", "w")

# store everything in one long list
long_string = []

# separate each sound into differemt elements
for line in oldfile:
    # remove \n at end
    line = line.strip("\n")
    # split into separate elements
    var1, var2 = line.split(",")
    # append both to long_string
    long_string.append(var1)
    long_string.append(var2)


# control variable
list_count = 1
# list of lists
min_pairs = []

# group min_pairs and store into list
for each in long_string:
    #  if in first counter
    if list_count == 1:
        # reset temp string and append current element
        temp = []
        temp.append(each)
        # update counter
        list_count += 1
    # else if counter = 2 or 3
    elif list_count == 2 or list_count == 3:
        # append current element
        temp.append(each)
        # update counter
        list_count += 1
    # if counter is 4
    else:
        # append current element
        temp.append(each)
        # write to list of lists
        min_pairs.append(temp)
        # reset counter
        list_count = 1

# dictionary
menu = {}
index = 1

# store each min_pair into dictionary
for pair in min_pairs:
    menu[index] = pair
    index += 1

# write to file
menu = str(menu)
newfile.write(menu)
    
# close everything
oldfile.close()
newfile.close()