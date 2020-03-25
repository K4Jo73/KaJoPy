import random
import sys

sys.path.append('./mod/')
#print(sys.path)
import FileHandler

print('\n' * 2)
print("Testing Custom Module Design")
print('\n' * 2)

FileHandler.ShowFile('README.md')

strFileContent = FileHandler.LoadFile()
print(strFileContent)

#FileHandler.CreateFile("File1.txt","My sample text\nand some more text")

FileHandler.DeleteFile("File1.txt")


#append to file