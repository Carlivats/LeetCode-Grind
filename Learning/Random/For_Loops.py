# Understanding For loops

for i in range(10):
    print(i)

# start, stop, step
# start, stop
# stop
x = ["s3","3rd","sdef"]
for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i,element)


# Slice
# sliced = [start:stop:step]
sliced = x[::-1]
print(sliced)

# Sets == Hashmaps
x = {'key': 4}

x['key2'] = 5

print(list(x.values()))

for key,value in x.items():
    print(key,value)




