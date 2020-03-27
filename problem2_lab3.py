def first_and_last_4(s):
    l = list(s)
    f = l[-4:]
    g = l[:4]
    h = (g + f)
    return (h)
s=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
z=first_and_last_4(s)
print(z)