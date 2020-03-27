def code():
    for i in range(50):
        if (i%3==0 and i%5==0):
            print(i,"FizzBuZZ")
            continue
        elif(i%3==0):
            print(i,"FiZZ")
            continue
        elif(i%5==0):
            print(i,"buZZ")
            continue
    print(i)
code()