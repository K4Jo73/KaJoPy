import os


# Function - Output the contents of a file
def ShowFile(filePath="LICENSE"):
    #Open and read the file
    objfile = open(filePath, "r+")
    text_in_file = objfile.read()
    print(text_in_file)



# Function - Return the contents of a file
def LoadFile(filePath="LICENSE"):
    if checkFile(filePath):
        objfile = open(filePath, "r+")
        text_in_file = objfile.read()
        return text_in_file
    return "File Not Found - Unable to load file: " + filePath



# Function - Create and populate a file
def CreateFile(filePath,fileContent):
    objfile = open(filePath, "wb")
    print("File Mode: " + objfile.mode)
    print("File Name: " + objfile.name)
    objfile.write(bytes(fileContent, 'UTF-8'))
    objfile.close()



# Function - Append to a file
def AppendFile(filePath,fileContent):
    if checkFile(filePath):
        objfile = open(filePath, "ab")
        print("File Mode: " + objfile.mode)
        print("File Name: " + objfile.name)
        objfile.write(bytes(fileContent, 'UTF-8'))
        objfile.close()
    return "File Not Found - Unable to append file: " + filePath



#Delete the file
def DeleteFile(filePath):
    os.remove(filePath)



# Function - Search the contents of a file
def SearchFile(filePath="LICENSE",searchFor=""):
    if checkFile(filePath):
        objfile = open(filePath, "r")
        lineNo = 0
        searchResults = "Searched for [" + searchFor + "] in file [" + filePath + "]\n\nSearch Results:\n" 
        fullFile = ""
        fileContent = objfile.readlines()
        for lineContent in fileContent:
            lineNo = lineNo + 1
            modifiedLine = formatLineWithNo(lineNo,lineContent)
            fullFile += modifiedLine
            if searchFor in lineContent: searchResults += modifiedLine
        searchResults += "\n\nFull File:\n" + fullFile
        return searchResults
    return "File Not Found - Unable to search file: " + filePath



def formatLineWithNo(LineNo=0,LineText=""):
    displayLineNo = "    " + str(LineNo)
    return "[" + displayLineNo[-4:] + "] " + LineText



def checkFile(filePath):
    try:
        with open(filePath) as f:
            return 1
    except IOError:
        return 0

