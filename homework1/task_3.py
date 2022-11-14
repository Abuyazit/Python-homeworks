def foo(n,m):
    a=[]
    if len(n)==len(m):
        for i in range(len(n)):
            a.append(n[i]*m[i])
        a.sort()
    else:
        for i in (n+m):
            if (n+m).count(i)>1:
                a.append(i)
        a.sort()
    return a



assert(foo([1, 2, 3, 3, 3], [-1, 2, 3])) == [2, 2, 3, 3, 3, 3]
assert(foo([1, 2, 3],[-1, 2, 0])) == [-1,0,4]
assert(foo([0,0,1, 0, 11, 8, 9], [-1,-2,-3,-4,-5,-7])) ==[0,0,0]
