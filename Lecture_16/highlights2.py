places = ['Mai Thai', "Arby's", "Johnny's Steakhouse",
          "Pickleman's", "Wendy's",
          "John's Grecian Delight"]

count = 0
for name in places:
    print(count,name)
    count += 1
    
for pos,name in enumerate(places):
    print(pos,name)
        
for pos,name in enumerate(places):
    print(f"{pos+1}. {name}")
        
quick = { "a" : 65, "b" : 70 }
for pos, value in enumerate(quick):
    print(pos,value)