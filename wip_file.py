
import sys
# sys.path.append('./mod/')
# sys.path.append('.\\mod\\')
sys.path.insert(0, './mod')
import fileHandler
import coreFeatures
import random
# import logging

# FORMAT = '[%(levelname)s]%(asctime)s: %(message)s'
# logging.basicConfig(filename="./logs/samplelogs.log", level=logging.INFO, format=FORMAT)


# print(sys.path)


coreFeatures.logging.debug(sys.path)
coreFeatures.setup_logging("./logs/")

print('_' * 50)
print('')
print("Testing Custom Module Design")
#print('\n' * 2)
print('_' * 50)

fileHandler.ShowFile('README.md')

#strFileContent = fileHandler.LoadFile()
# print(strFileContent)

#fileHandler.CreateFile("File1.txt","My sample text\nand some more text")
#fileHandler.AppendFile("File1.txt","\nThis is new text appended to the file\nand some more text")


#MySearchResults = fileHandler.SearchFile("LICENSE","public")
# print(MySearchResults)

MySearchResults = fileHandler.SearchFile("File1.txt", "and")
# print(MySearchResults)
coreFeatures.logging.info(MySearchResults)

# fileHandler.DeleteFile("File1.txt")

fileHandler.LoadCSV("test.csv")

coreFeatures.logging.error("whoops")

coreFeatures.logging.warning("dont dare")

coreFeatures.logging.critical("Oh Christ!")

try:
    x = 10
    y = 0
    Res = x / y
# except ZeroDivisionError:
except Exception:
    coreFeatures.logging.exception("This is used in try catch scenarios!")


