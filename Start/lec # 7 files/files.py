file = open("demo.txt", "r")
# data = file.read()
# print(data)
line1 = file.readline()
print(line1)

line2 = file.read()
print(line2)

file.close()
