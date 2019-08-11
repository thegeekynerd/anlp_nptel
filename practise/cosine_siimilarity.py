d1 = [0.1,0.1,0.0,0.1]
d2=[0.0,0.1,0.9,0.9]
d3=[0.1,0.1,0.0,0.02]
q=[0.1,0.001,0.0,0.2]

cosined = []

def find1():
    ab=0
    a2=0
    b2=0
    d=0
    for i in range(0,4):
        ab+=d1[i]*q[i]
        a2=d1[i]*d1[i]
        b2=q[i]*q[i]
        d+=pow(a2,0.5)*pow(b2,0.5)
    return d

def find2():
    ab=0
    a2=0
    b2=0
    d=0
    for i in range(0,4):
        ab+=d2[i]*q[i]
        a2=d2[i]*d2[i]
        b2=q[i]*q[i]
        d+=pow(a2,0.5)*pow(b2,0.5)
    return d

def find3():
    ab=0
    a2=0
    b2=0
    d=0
    for i in range(0,4):
        ab+=d3[i]*q[i]
        a2=d3[i]*d3[i]
        b2=q[i]*q[i]
        d+=pow(a2,0.5)*pow(b2,0.5)
    return d
