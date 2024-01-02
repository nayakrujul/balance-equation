from itertools import product
from collections import defaultdict

def count_up(p, q, r):
    return product(*[range(p,q+1)]*r)

def force_solve(lhs, rhs, limit=10):
    l = len(lhs) + len(rhs)
    for mults in count_up(1, limit, l):
        nl, nr = lhs.copy(), rhs.copy()
        lm, rm = mults[:len(lhs)], mults[len(lhs):]
        le, re = defaultdict(int), defaultdict(int)
        for el, ml in zip(nl, lm):
            for x in el.split():
                en, n = x.split('_')
                le[en] += int(n) * ml
        for er, mr in zip(nr, rm):
            for x in er.split():
                en, n = x.split('_')
                re[en] += int(n) * mr
        if le == re:
            return mults
    return False

def process(s):
    r = []
    for c in s:
        if c.isupper():
            if r and '_' not in r[-1]:
                r[-1] += '_1'
            r.append(c)
        elif c.islower():
            r[-1] += c
        else:
            r[-1] += '_' + c
    if r and '_' not in r[-1]:
        r[-1] += '_1'
    return ' '.join(r)


def interface(l, r, lim=10):
    ls, rs = l.replace(' ', '').split('+'), r.replace(' ', '').split('+')
    sol = force_solve([process(x) for x in ls], [process(y) for y in rs], lim)
    if not sol:
        return False
    lm, rm = sol[:len(ls)], sol[len(ls):]
    return ('+'.join(str(i)*(i>1)+j for i,j in zip(lm,ls)),
            '+'.join(str(i)*(i>1)+j for i,j in zip(rm,rs)))
