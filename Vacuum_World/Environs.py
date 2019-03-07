import numpy as np

class State():
    def __init__(self,x,y):
        self.grid = np.zeros((x,y))


class MiniMax2(State):
    def __init__(self, dirt_locs):
        x, y = 2,2
        State.__init__(self,x,y)
        if dirt_locs is not None:
            for loc in dirt_locs:
                self.grid[loc[0],loc[1]] = 1


class LimitedRandom(State):
    def __init__(self):
        x, y = np.random.randint(8,16), np.random.randint(8,16)
        State.__init__(self,x,y)
        for a in range(x):
            for b in range(y):
                if 100*np.random.random() < 5:
                    self.grid[a,b] = 1


def unpack(lst, x, *args):
    nulst =[]
    x = x if type(x)==list else [x]
    if not lst:
        nulst = [[x_0] for x_0 in x]
    else:
        nulst = [l+[x_0] for l in lst for x_0 in x]
    if args:
        return unpack(nulst, *args)
    else:
        return nulst

def multiverse(state, *args):
    verse = []
    lst = unpack([], *args)
    for variant in lst:
        verse.append(state(*variant))
    return verse

def MiniMax2Package():
    locs = [None,
            [(0,0)],
            [(0,1)],
            [(1,0)],
            [(1,1)],
            [(0,0),(0,1)],
            [(0,0),(1,0)],
            [(0,0),(1,1)],
            [(0,1),(1,0)],
            [(0,1),(1,1)],
            [(1,0),(1,1)] ]
    return multiverse(MiniMax2,locs)
