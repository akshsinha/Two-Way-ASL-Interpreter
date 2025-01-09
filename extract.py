import os
import shutil
def getListOfFiles(dirName): #retrieves files with extension .webp and renames them
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath) #uses recursion
        else:
            if(fullPath.endswith('.webp')):
                allFiles.append(fullPath)
                
    return allFiles

dirname ='/Users/akshsinha/Desktop/two-way-sign-language-translator-master/'
dest="/Users/akshsinha/Desktop/two-way-sign-language-translator-master/gif_data/"

data=getListOfFiles(dirname)
for i in range(len(data)):
    fname=dest+str(i)+".webp"
    shutil.copyfile(data[i], fname)
