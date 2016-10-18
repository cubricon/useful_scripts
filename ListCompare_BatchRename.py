"""

This script will take a list that you have generated, such as a text file
and compare any 3 digits per line of text to any 3 digits in a set of files.
for example, if you had a bunch of JPEG files but wanted to rename your picks
i.e. "img_005.jpg" --> "pick_img_005.jpg". The script will leave any files
that are not on the list alone.

"""

import os
import re


os.chdir ('/Users/anthonydias/Python') #set your working directory

n = os.getcwd() 

f_file = open('top_picks.txt', 'r') #chose your file here, format should be a list

for line in f_file:

    for dir_file in os.listdir(n):
        a = re.findall('\d{1,3}', line)
        b = re.findall('\d{1,3}', dir_file)
        
        if a == b:
            
            new_name = 'pick_'+dir_file
            print new_name

# WARNING, NOT UNDOABLE! UNCOMMENT THE NEXT LINE TO RENAME YOUR FILES
#            os.rename (dir_file, new_name)
            

f_file.close ()

