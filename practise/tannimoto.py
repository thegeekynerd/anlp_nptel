def intersection(a,b):
    inters = []
    for i in range(len(a)):
        if (a[i] == b[i]):
            inters.append(a[i])
    return inters
def tanimoto(a,b):
    c = intersection(a,b)
    return ((float)(len(c))/(len(a)+len(b)-len(c)))

d1 = [0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0]
d2 = [0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1]
d3 = [0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0]
