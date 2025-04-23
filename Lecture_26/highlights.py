# highlights from lecture 26

stuff = dict(one=10, two=20, three=30, four=40)
thing = {"one":10, "two":20, "three":30, "four":40}
# 
# for v in stuff.values():
#     print(v)
# for k in stuff.keys():
#     print(k)
# for k,v in stuff.items():
#     print(f"{k} has a value of {v}")
# for k in stuff:
#     print(f"{k} has a value of {stuff[k]}")
    
temps = { "w1" : [56, 76, 81, 32, 1, 88, 88],
          "w2" : [ 1, 2, 3, 4, 5, 6, 7 ],
          "w3" : [ 10, 20, 30, 40, 50, 60, 70, 80],
          }

# print(temps)
# 
# temps["w4"] = [67, 43]
# print(temps)
# temps["w5"] = [67]
# print(temps)
# temps["w6"] = "too hot"
# print(temps)
# temps["w5"].append(68)
# print(temps)

temps = { "w1" : [56, 76, 81, 32, 1, 88, 88],
          "w2" : [ 1, 2, 3, 4, 5, 6, 7 ],
          "w3" : [ 10, 20, 30, 40, 50, 60, 70, 80],
          }

for w,t in temps.items():
    print("="*20)
    print(w)
    print(t)
    for a_temp in t:
        print(a_temp, end=' and ')
    print()
    print(sum(t))
    print(len(t))
    print(sum(t)/len(t))
    print()
# # 
# # 
# 
# 
# 
# 
# 
# 
# 
# 
concerts = {
    'CHI' : {
            'address' : '455 N 10th St, Omaha, NE 68102',
            'capacity' : 18975,
            'shows' : ['Kelsea Ballerini', 'Linkin Park']
        },
    'Slowdown' : {
            'address' : '729 N 14th St, Omaha, NE 68102',
            'capacity' : 750,
            'shows' : ['King Buffalo', 'Michigan Rattlers', 'The Velveteers']
        },
    'Orpheum' : {
            'address' : '409 S 16th St, Omaha, NE 68102',
            'capacity' : 2600,
            'shows' : ['The Nutcracker', 'Peter Pan', "Kimberly Akimbo"]
        }
    }

# 
# print(concerts.keys())
# print(concerts.values())
# print(concerts["Slowdown"]["address"])
# print(concerts["Slowdown"]["shows"][1])
# # 
# # 
for venue in concerts:
   print()
   print(venue)
   print("Address:", concerts[venue]['address'])
   print("Capacity:", concerts[venue]['capacity'])
   print("Shows: ")
   for s in concerts[venue]['shows']:
       print(f"{s:>20}")
    
