import functools
import math

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = functools.reduce(op.mul, range(n, n-r, -1))
    denom = functools.reduce(op.mul, range(1, r+1))
    return numer//denom

def p_exactly_k(p, n, k):
    not_p = 1.0 - p
    return (p**k) * (not_p**(n-k)) * ncr(n, k)

def lia(kk, nn):
    p_both_het = 0.25
    p_total = 0.0
    total_children = 2**kk
    for i in range(nn, total_children+1):
        p_total += p_exactly_k(p_both_het, total_children, i)
    return p_total

# def lia(kk, nn):
#     initial = [0.0, 1.0, 0.0]
#     state = initial
#     num_children = 1
#     for i in range(kk):
#         state = step(state)
#         num_children *= 2
#         # print(state)
#         assert math.isclose(sum(state), 1.0, rel_tol=1e-5)


#     p_het = state[1]
#     p_both_het = p_het * p_het


#     # TODO: fix for nn != 1
#     return p_both_het


# def step(state):
#     # [dom/dom, dom/rec, rec/rec]
#     p_dd = state[0] * state[0] + 0.5 * state[0] * state[1] + 0.25 * state[1] * state[1]
#     p_dr = state[0] * state[2] + 0.5 * state[1] * state[1] + 0.5 * state[0] * state[1] + 0.5 * state[2] * state[1]
#     p_rr = state[2] * state[2] + 0.5 * state[2] * state[1] + 0.25 * state[1] * state[1]
#     return [p_dd, p_dr, p_rr]

# def step(state):
#     p_dd = state[0] * 0.5 + state[1] * 0.25
#     p_dr = state[0] * 0.5 + state[1] * 0.5 + state[2] * 0.5
#     p_rr = state[2] * 0.5 + state[1] * 0.25
#     return [p_dd, p_dr, p_rr]

print(lia(0,1))
print(lia(5,7))

assert lia(2, 1) >= 0.683
assert lia(2, 1) <= 0.685
