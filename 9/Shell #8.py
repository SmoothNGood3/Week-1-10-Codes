def printAll(seq):
    if seq:
        print (seq[0])
        printAll(seq[1:])
printAll("Hi, I'm Camden!")
printAll((1,2,3,4,5,6,7,8,9,10))

