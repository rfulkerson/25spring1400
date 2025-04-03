def what(x):
    print("Hello")
    print(x)
    x[1] = 10
    print(x)
   
def who(a,b,c,d,e,f,g,h,i):
    pass

def calc_taxes(total, tax_rate=0.07):
    return total + total * tax_rate

def do_the_thing():
    return 6

def do_another():
    return ("Hello", 5.6, 6)

y = do_another()
z,zz,zzz = do_another()

# value = calc_taxes(9.97, 0.00)
# value = calc_taxes(9.97)
# who(a=j,b=k,c=l,d=m,e=n,f=o,g=p,i=r,h=q)
# 
# print("Hello", "there", "what", end=' ... ')
    
# a = 5
# what(a)
# print(a)

b = [6, 7, 8]
# print(b)
what(b[:])
# print(b)