
def mystery(word):
    count = 0
    vowels = "aeiou"
    for letter in word:
        if letter in vowels:
            count += 1
    return count

x = mystery("HEllo")
print(x)
# x = mystery("Supercalifragilisticexpealidocious")
# print(x)
