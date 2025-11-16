fruits = ["Cherry", "Apple", "Pear"]

#INDEXING
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] #this will be "Pear"
print(fruits[-1]) #INDEXING

# MODIFYING
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange" #MODIFYING
print(fruits[0])
print(fruits)

#APPENDING
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits will now become ["Cherry", "Apple", "Pear", "Orange"]
print(fruits) #APPENDING

#APPENDING USING EXTEND ( we can add more than one item)
fruits = ["Cherry", "Apple", "Pear"]
fruits.extend(["Orange","banana"])
# fruits will now become ["Cherry", "Apple", "Pear", "Orange","banana"]
print(fruits)


