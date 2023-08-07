keys = ["key1", "key2", "key3"]
names = ["name1", "name2", "name3"]
books = ["book1", "book2", "book3"]

for i in range(len(keys)):
    print(f"{i+1}. Key: {keys[i]}, Name: {names[i]}, Book: {books[i]}")

hot_keys = [keys,names,books]
#hot_keys[0] = ["key1", "key2", "key3"]
#hot_keys[1] = ["name1", "name2", "name3"]
hot_keys[2] =["book11", "book22", "book33"]
#hot_keys[3] =["book11", "book22", "book33"]

for i in range(len(hot_keys)):
    print(f"{i+1}. Key: {hot_keys[i]}, Name: {hot_keys[i]}, Book: {hot_keys[i]}") 
hot_keys[1]="namealea"
#hot_keys[1].append("jammaa")    
print(hot_keys[1][3])

#input_two = input("Program 1: ")
#for i in range(len(keys)):


check_key = input("change which key: ")
change_key = ""

#Check if the user input matches any of the keys
for i in range(len(keys)):
    if check_key == keys[i]:
# Get the user input for the new key
        change_key = input(f"{'\033[34m'}{keys[i]}{'\033[0m'} {names[i]} {books[i]}: ")
# Update the key
keys[i] = change_key
# Print the updated key, name, and book
print(f"Key: {keys[i]}, Name: {names[i]}, Book: {books[i]}")
break

#Print the updated list of keys, names, and books
for i in range(len(keys)):
print(f"{i+1}. Key: {keys[i]}, Name: {names[i]}, Book: {books[i]}")    
        