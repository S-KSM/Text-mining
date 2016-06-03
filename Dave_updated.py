
# coding: utf-8

# # Project Dave!
# 
# 
# ## How the inputs should be?
# 
# The Keywords should be in different lines of a ** *.dat** file. In order to achieve this, just open a text editor, NotePad++ works very nice on Windows and it is free.
# 
# You documents are supposed to be a ** *.txt ** file.
# 
# The files that needs to be analyzed, should be in the same folder as your code.
# 
#     The code lines are commented to show what they do.

# In[2]:

import glob
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

path_documents = "*.txt"
path_inp = "*.dat"


# In[3]:

### function that finds the occurance of a keyword in a line.
def findSectionOffsets(text,pattern):
    indexes = []
    startposition = 0
    text = str(text)
    pattern = str(pattern)
    x = True

    while x == True:
        i = text.find(pattern, startposition)
        if i == -1: x = False
        indexes.append(i)
        startposition = i + 1

    return indexes


### Reads Keywords from your file
for file in glob.glob(path_inp):
    f = open(file,"r",encoding='utf-8')
    inp = f.read()
    keywords = [line for line in inp.splitlines()] # makes a list of keywords
    
stop_words = set(stopwords.words('english')) ### Make a list of stopwords            


# In[11]:

### total is a dictionary that is going to store everything
total = {}
dict_top100 = {}
final_wordfrequency = {}
for file in glob.glob(path_documents):
    total[file]={}
    

    
    f = open(file,"r",errors = "surrogateescape") # In case there is an error with the formatting, it tries to handle
    myfile = f.read() #Reads the file
    mysentences = sent_tokenize(myfile) # extract sentences
    mywords = word_tokenize(myfile) # extract words
    
    filtered_mywords = [w for w in mywords if not w in stop_words]

    for line in mysentences:
        #print(type(line))
        for key in keywords:
            if key not in total[file]:
                total[file][key]=[]
            else:
                #print(1)
                indices = findSectionOffsets(str(line),str(key))
                #print(indices)
                if len(indices) > 1:
                    #for i in range(len(indices)):
                    total[file][key].append(line[indices[0]-50:indices[0]+50+len(key)])

            
df = pd.DataFrame(total)            



final_output = open("finaloutput.csv","w")
final_output.write("FileName, Keyword, Sentence\n")
for keyword in keywords:
    col_key = keyword
    for column in df.columns:
        col_file = column
        for i in range(len(total[column][keyword])):
            ### we are removing the commas and next line as well as byte characters for readability of the output
            sentence = str(total[column][keyword][i].replace("\n"," ").replace(","," ")).encode('ascii','ignore')
            sentence = sentence.decode("utf-8")
            if len(sentence) > 20:
                final_output.write(col_file + ", " + col_key + ", " + sentence + "\n")
            else:
                pass

final_output.close()


df_temp = pd.read_csv("finaloutput.csv")
grouped = df_temp.groupby([' Keyword','FileName'])
df_temp2 = grouped.count()
df_temp2.columns = ['Frequency']
df_temp2.to_csv("Frequency_updated.csv")


# In[5]:

keywords


# In[ ]:



