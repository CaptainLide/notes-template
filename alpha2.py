import os 
subject = input("Hello AJ, what subject are you adding a note for?: ")
title = input("Enter a brief title for the context of the note: ")

space = "_" # lazy formatting
filetype = ".txt" # edit this in case you don't want the file type to be .txt

# you can edit the directory of where your notes will go here
cmd = 'touch /home/lide/Documents/Misc/notes-template/test_notes/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype
os.system(cmd)

# this will be the fun part where template can be customized accordingly 
w = 'echo Subject = '+ subject + ' >> /home/lide/Documents/Misc/notes-template/test_notes/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype + '&& echo Title = ' + title + ' >> /home/lide/Documents/Misc/notes-template/test_notes/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype + ' && echo Date = $(date +"%m-%d-%y") >> /home/lide/Documents/Misc/notes-template/test_notes/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype+ '&& echo "\nContent:" >> /home/lide/Documents/Misc/notes-template/test_notes/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype
os.system(w)

# for now i'm forcing user to use VIM but later on i will make it so that they can choose what application to open
cmd1 = 'vi /home/lide/Documents/Misc/notes-template/test_notes/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype 
os.system(cmd1)
# make sure to change the directory on 'cmd1' as well... 

# this will be where files will be organized 