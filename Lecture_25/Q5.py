where = { "UNO" : 'Omaha',
          "UNK" : 'Kearney',
          "UNL" : 'Lincoln',
          "UNMC" : "Omaha" }

for x in range(3):
    which = input("Delete? ")
    del where[which]
print(where)
