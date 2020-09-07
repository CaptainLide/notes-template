import os 
print("Here are a list of the current directories")
for x in os.listdir('/home/lide/Documents/Subjects'):
    print(x)

subject = input("\n\nHello AJ, what subject are you adding a note for?: ")
title = input("Enter a brief title for the context of the note: ")

space = "_" # lazy formatting
filetype = ".txt" # edit this in case you don't want the file type to be .txt

# if-statement (if command feeds back 1 then folder was not created if there was 0 error then proceed with further instruction)
check = os.system('cd /home/lide/Documents/Subjects/'+subject)
if check == 0:
    print("Creating File...")
    os.system('touch /home/lide/Documents/Subjects/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype)
else:
    print("Creating Folder and Files...")
    os.system('mkdir /home/lide/Documents/Subjects/'+subject+'&& touch /home/lide/Documents/Subjects/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype)

# create template for .txt
t = 'echo Subject = '+ subject + ' >> /home/lide/Documents/Subjects/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype + '&& echo Title = ' + title + ' >> /home/lide/Documents/Subjects/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype + ' && echo Date = $(date +"%m-%d-%y") >> /home/lide/Documents/Subjects/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype+ '&& echo "\nContent:" >> /home/lide/Documents/Subjects/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype
os.system(t)

# goto VIM
cmd1 = 'vi /home/lide/Documents/Subjects/'+subject+'/$(date +"%m-%d-%y")"_"'+subject+space+title+filetype
os.system(cmd1)




