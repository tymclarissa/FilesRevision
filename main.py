with open("code.txt") as f:
     impt = f.read()

print (impt) 
list1 = impt.split('/n')
print(list1)

with open ("important.txt", "w") as f:
      f.write("This fille has be written to")

