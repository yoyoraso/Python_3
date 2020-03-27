def check(element,tup):
    if element in tup:
        print(True)
    else:
        print(False)
    return (element,tup)
tupler =  ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
z = check('w',tupler)
print(z)