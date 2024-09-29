#Creating a Dictionary
#Used this {} to creat Diction
Student = {
    "Name":"Ammar",
    "F/name":"Anwer",
    "Class":"XII",
    "Section":"A",
    "Location":"Karachi",
    "Phone":3202595322,
}

# Here is access to the dictionary
print(Student["Name"])

# These are methods

# Method	Description	Example
# get(key)	Returns the value for the specified key. If the key doesn’t exist, returns None.	student.get("name") → "Ammar"
# keys()	Returns a list of all the keys in the dictionary.	student.keys() → dict_keys(['name', 'age'])
# values()	Returns a list of all the values in the dictionary.	student.values() → dict_values(['Ammar', 20])
# items()	Returns a list of all key-value pairs (as tuples).	student.items() → dict_items([('name', 'Ammar'), ('age', 20)])
# pop(key)	Removes the specified key and returns its value.	student.pop("age") → 20
# popitem()	Removes and returns the last inserted key-value pair.	student.popitem() → ('age', 20)
# clear()	Removes all items from the dictionary.	student.clear() → {}
# update()	Updates the dictionary with key-value pairs from another dictionary or iterable.	student.update({"age": 21}) → {'name': 'Ammar', 'age': 21}
# fromkeys()	Creates a new dictionary from a sequence of keys, with all values set to a specified value.	dict.fromkeys(['a', 'b'], 0) → {'a': 0, 'b': 0}
# setdefault()	Returns the value of a key. If the key does not exist, it inserts the key with a default value.	student.setdefault("course", "Math") → 'Math' (also adds 'course': 'Math' if not present)

# Get method 
print("Get method", Student.get('Phone'))

# Key method 
print("Keys method", Student.keys())

# Values method 
print("value method", Student.values())

# Items method 
print("Items method", Student.items())

# pop method 
print("POP method", Student.pop('Phone'))

# Clear method 
print("Clear method", Student.clear())


# Adding and Updating Items 
Student["Location"] = "Islamabad"
print("Adding and Updating", Student)

# Deleting Items
del Student["Location"]
print("Deleting Item", Student)

# Looping Through Dictionary
# 1) Keys

for key in Student.keys():
    print(key)
    
# 2) Values

for value in Student.values():
    print(value) 

# 3) Key-value pairs

for key, value in Student.items():
    print(key, ":", value)