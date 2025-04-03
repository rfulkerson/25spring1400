def song_length(mins, sec):
    calc = mins * 60 + sec
    return calc
    
mn = int(input("Min: "))
sc = int(input("Sec: "))

r = song_length(sec=sc,mins=mn)
print(f"Length: {r}")

# print("minutes is:", m, end= '......')
# print("second is:", s)
