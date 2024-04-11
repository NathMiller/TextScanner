document = "the quick brown brown brown fox"
seek = input("Please enter the word you want replaced: ")
replace1 = input("Please enter the first replacement string: ")
replace2 = input("Please enter the second replacement string: ")

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

print(instances)
print(updatedDoc)
