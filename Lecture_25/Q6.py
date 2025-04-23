stuff = input().split()
d = {}
for x in range(0,len(stuff),2):
    d[stuff[x]] = stuff[x+1]

print(d.get('What','Blue'))
if '25' in d:
    print(d['25'])
#print(d['25'])
print(d.get('25',"Blue"))




# if "25" in d:
#     print(d['25'])
# else:
#     print("Blue")
# if "What" in d:
#     print(d['What'])
# else:
#     print("Blue")
