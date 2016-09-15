# checks file_type of a given file and prints to terminal

import magic
import os

# iterate over every file in given directory
for file in os.listdir("italian_media"):
    # print file name and file info
    print(file + ": " + magic.from_file("italian_media/{}".format(file)))