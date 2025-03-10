# my_list = ["Bob","Anna","Jeff","Jose","Sally"]

# pos = 0
# while pos < len(my_list):
#     if my_list[pos] == "Francesca":
#         print(f"I found Francesca at position {pos}!")
#     else:
#         print(f"I didn't find Francesca")
#     pos += 1
#

# my_list = ["Bob","Anna","Jeff","Jose","Sally"]

# pos = 0
# while pos < len(my_list):
#     if my_list[pos] == "Bob":
#         found = True
#     else:
#         found = False
#     pos += 1

# my_list = ["Bob","Anna","Jeff","Jose","Sally"]
# 
# pos = 0
# found = False
# while pos < len(my_list):
#     if my_list[pos] == "Bob":
#         found = True
#     pos += 1
# if found == True:
#     print("I found the person you're looking for!")
# else:
#     print("I didn't find the person you're looking for!")
#     
# 
# if "Sue" in my_list:
#     print("I found Sue!")
# else:
#     print("I didn't find Sue!")
#     
# if "hello" in "i said hello":
#     print("hello is in the string!")
    
    
x = "hello"
y = "hello"

print(id(x))
print(id(y))

if x is y:
    print("they're the same thing!")

a = 5000
b = 5000
c = 2500 + 2500

print(id(a))
print(id(b))
print(id(c))

b = 5000
print(id(b))
if a is b:
    print("a is b!")
if a == b:
    print("a == b!")

# my_list = ["Bob","Anna","Jeff","Jose","Sally"]
# 
# x = 0
# while x < len(my_list):
#     print(my_list[x])
#     x += 1
#     
# for name in my_list:
#     print(name)
    
# word = "supcalifragilisticexpealidocious"
# 
# vowels = 0
# for letter in word:
#     #if letter == 'a' or letter == 'e' or letter =='i' or letter == 'o' or letter == 'u':
#     if letter in "aeiou":
#         vowels += 1
# print(f"there are {vowels} vowels in {word}")
