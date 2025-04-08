phrase = "There's a lady who's sure all that glitters is gold"
search = "guld"

print(phrase.find(search))

if phrase in search:
    print("Found it A!")
if phrase.find(search) >= 0:
    print("Found it B!")
if search == phrase:
    print("Found it C!")
#if phrase contains search:
#    print("Found it!")
