document = "the quick brown brown brown brown brown brown brown brown fox"
seek = input("Please enter the word you want replaced: ")
replace1 = input("Please enter the first replacement string: ")
replace2 = input("Please enter the second replacement string: ")

seekQuantity = document.count(seek)
instances = []

for i in range(seekQuantity):
    if i % 2 == 0:
        instances.insert(i, [i, replace1])

    else:
        instances.insert(i, [i, replace2])

print(instances)

