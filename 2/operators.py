from functools import partial
import logging

class Infix(object):
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        return self.func(other)

    def __ror__(self, other):
        return Infix(partial(self.func, other))

    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q):
    ret = eval("not p or q")
    return ret

@Infix
def iff(p, q):
    ret1 = eval("not p or q")
    ret2 = eval("not q or p")
    ret = eval("ret1 and ret2")
    return ret

@Infix
def xor(p, q):
    ret1 = eval("not p and q")
    ret2 = eval("p and not q")
    ret = eval("ret1 or ret2")
    return ret

@Infix
def eq(p, q):
    ret1 = eval("p and q")
    ret2 = eval("not p and not q")
    ret = eval("ret1 or ret2")
    return ret


