import time

filePath = r"C:\Users\Nathan\Documents\targetFile.txt"
updatedFile = r"C:\Users\Nathan\Documents\updatedFile.txt"
with open(filePath, 'r') as file:
    document = file.read()


seek = input("Please enter the word you want replaced: ")
replace1 = input("Please enter the first replacement string: ")
replace2 = input("Please enter the second replacement string: ")
print("-------------------")

seekQuantity = document.count(seek)
updatedDoc = document
instances = []

for i in range(seekQuantity):
    if i % 2 == 0:
        instances.insert(i, [i, replace1])
        updatedDoc = updatedDoc.replace(seek, replace1, 1)
    else:
        instances.insert(i, [i, replace2])
        updatedDoc = updatedDoc.replace(seek, replace2, 1)

f = open(updatedFile, "w")
f.write(updatedDoc)
f.close()

print("Replacing values...")
print("-------------------")
time.sleep(2)
print("You will find a new copy of your file with the changes made in the original folder.")

