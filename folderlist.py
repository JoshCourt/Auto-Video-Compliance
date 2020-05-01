
import os
import sys
## Make Log File
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass

sys.stdout = Logger()
## Make Log File

'''
https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/
    For the given path, get the List of all files in the directory tree
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

# "Y:"
include_suffix = (".mp4", ".mpg", ".mpeg", ".mov", ".mkv", ".avi")
def get_list_go(dir):

    dirName = str(dir)

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)

    # Make a Record of the files
    with open("Files_list.txt", "w+") as file:
        for elem in listOfFiles:
            #print(elem.encode("utf-8"))
            if elem.endswith(include_suffix):
                file.write(str(elem.encode("utf-8"))+"\n")
    file.close()

    #Print the files
    #for elem in listOfFiles:
    #    print(elem.encode("utf-8"))

    print ("****************")

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]






#if __name__ == '__main__':
#    get_list_go()
