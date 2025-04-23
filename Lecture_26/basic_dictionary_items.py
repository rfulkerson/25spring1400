dictionary = { "what" : "hi", "who": "Yo" }

# for thing in dictionary:
#     print(thing)
#     print(dictionary[thing])
    
# for key,val in enumerate(dictionary):
#     print(key,val)
#     
# for key in dictionary.keys():
#     print(key)
#     
# for val in dictionary.values():
#     print(val)

for key,val in dictionary.items():
    print(key,val)
# 
for key in dictionary:
    print(key,dictionary[key])
