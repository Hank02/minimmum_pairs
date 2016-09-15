# open files
oldfile = open("minpairs.txt", "r")
newfile = open("word_list.txt", "w")

# loop over every lien in file
for line in oldfile:
    # split line using "-"
    s1, s2, s3 = line.split("-")
    # target word is in s3, so split it using "."
    w1, w2 = s3.split(".")
    # mark locaition of \n
    index = w1.find("\n")
    # append "," and word at location of \n and then add back \n
    entry = line[:index] + ',' + w1 + "\n"
    # write to file
    newfile.write(entry)

    

# close everything
oldfile.close()
newfile.close()