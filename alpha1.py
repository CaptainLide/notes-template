import os 
subject = input("Hello AJ, what subject are you adding a note for?: ")
title = input("Enter a brief title for the context of the note: ")

space = "_" # lazy formatting
filetype = ".txt" # edit this in case you don't want the file type to be .txt

# if-statement (if command feeds back 1 then folder was not created if there was 0 error then proceed with further instruction)
check = os.system('cd /home/lide/Documents/'+subject)
if check == 0:
    print("Creating File...")
    os.system('touch /home/lide/Documents/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype)
else:
    print("Creating Folder and Files...")
    os.system('mkdir /home/lide/Documents/'+subject+'&& touch /home/lide/Documents/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype)


    




