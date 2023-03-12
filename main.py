def M(a):
    n=list()
    rez=""
    for i in a:
        i=str(i)
        n.append(i)
    n.sort(reverse=True)
    for j in n:
        rez=rez+j
    rez=int(rez)
    print(rez)

M([5,76,346,8639,9])