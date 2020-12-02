#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    e= [l.strip() for l in f.readlines()]

def ip(e):
    r,l,p = map(lambda x: x.strip(':'), e.split(' '))
    r1,r2 = next((int(r1),int(r2)) for r1,r2 in [r.split('-')])
    return r1, r2, l, p

def a1(e):
    y = 0
    for i in e:
        r1,r2,l,p = ip(i)
        if p.count(l) >= r1 and p.count(l) <= r2: y += 1
    return y

def a2(e):
    y = 0
    for i in e:
        r1,r2,l,p = ip(i)
        c1,c2 = p[r1-1],p[r2-1]
        if bool(c1 == l) ^ bool(c2 == l): y += 1
    return y

print(a1(e))
print(a2(e))
