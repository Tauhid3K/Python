capitals = {
    'Afghanistan': 'Kabul',
    'Chaina': 'Beijing',
    'Russia': 'Moscow',
    'USA': 'Washington, D.C.',} #dictionary = key:value pairs

#print(dir(capitals))
#print(help(capitals))

print(capitals.get('Russia')) #Get value by key
print(capitals.get('Japan'))  #None if key not exist

if capitals.get('Chaina'): #Check if key exist
    print("The capital is exist")
else:
    print("The capital is not exist")
    
capitals.update({'Germany': 'Berlin'})  #Add new key:value pair
capitals.update({'USA': 'Detroit'})     #Update value for existing key
capitals.pop('Chaina') #Remove key:value pair by key
capitals.popitem()     #Remove last inserted key:value pair
#capitals.clear()       #Remove all key:value pairs

print(capitals)

keys = capitals.keys()       #Get all keys

for key in capitals.keys():  #Iterate through keys
    print(key)

print(keys)

vlues = capitals.values()       #Get all values

for value in capitals.values(): #Iterate through values
    print(value)
    
print(vlues)

items = capitals.items()        #Get all key:value pairs
print(items)

for key, value in capitals.items():         #Iterate through key:value pairs
    print(f"Key: {key} Value: {value}")