for x in range(15,25):
    for r in range(2,x):
        if x%r==0:
            break
    else:
        print(x,end=' ')    