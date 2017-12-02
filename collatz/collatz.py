def collatz(z):
    while(z!=1):
        if z%2==0:
           z=z//2
        else:
            z=z*3+1
        print z
