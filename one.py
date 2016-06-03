import os;
import sys;
filePathSrc="C:/Users/Shobeir/Desktop/Fiverr/20160222/David/"
for root, dirs, files in os.walk(filePathSrc):
    for fn in files: 
        if fn[-4:] == '.txt':     
            notepad.open(root + "\\" + fn)      
            notepad.runMenuCommand("Encoding", "Convert to UTF-8")
            notepad.save()
            notepad.close()