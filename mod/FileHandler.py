import os


# Function - Output the contents of a file
def ShowFile(filePath="LICENSE"):
    #Open and read the file
    objfile = open(filePath, "r+")
    text_in_file = objfile.read()
    print(text_in_file)



# Function - Return the contents of a file
def LoadFile(filePath="LICENSE"):
    #Open and read the file
    objfile = open(filePath, "r+")
    text_in_file = objfile.read()
    return text_in_file



# Function - Create an populate a file
def CreateFile(filePath,fileContent):
    objfile = open(filePath, "wb")
    print(objfile.mode)
    print(objfile.name)
    objfile.write(bytes(fileContent, 'UTF-8'))
    objfile.close()



#Delete the file
def DeleteFile(filePath):
    os.remove(filePath)
