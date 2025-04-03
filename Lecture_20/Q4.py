def song_length_in_sec(mins, sec):
    calc = mins * 60 + sec
    return calc
    
mn = int(input("Min: "))
sc = int(input("Sec: "))

r = song_length_in_sec(sc,mn)


print(f"Length: {r}")