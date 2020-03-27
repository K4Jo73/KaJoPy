
import random
import sys

sys.path.append('./mod/')
#print(sys.path)
import FileHandler

print('_' * 50)
print('')
print("Testing Custom Module Design")
#print('\n' * 2)
print('_' * 50)

#FileHandler.ShowFile('README.md')

#strFileContent = FileHandler.LoadFile()
#print(strFileContent)

#FileHandler.CreateFile("File1.txt","My sample text\nand some more text")
#FileHandler.AppendFile("File1.txt","\nThis is new text appended to the file\nand some more text")


#MySearchResults = FileHandler.SearchFile("LICENSE","public")
#print(MySearchResults)

MySearchResults = FileHandler.SearchFile("File1.txt","and")
print(MySearchResults)


#FileHandler.DeleteFile("File1.txt")


#append to file