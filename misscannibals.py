# SPDX-License-Identifier: GPL-2.0-only
# Copyright (c) Amy Parker, Kevin Liu, and Ramiro Aispuro

from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0,0,False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    # Note: assumes that the action is legal
    def result(self, state, action):
        d = -1 if state[2] else 1
        nM = action.count("M")
        nC = action.count("C")
        return (state[0]+nM*d, state[1]+nC*d, not state[2])

    def actions(self, state):
        d = -1 if state[2] else 1
        res = []
        for n in [
            ("MM", (state[0]+2*d, state[1])),
            ("M", (state[0]+d, state[1])),
            ("MC", (state[0]+d, state[1]+d)),
            ("C", (state[0], state[1]+d)),
            ("CC", (state[0], state[1]+2*d))
            ]:
            nM = n[1][0]
            nC = n[1][1]
            if nM < 0:
                continue
            if nC < 0:
                continue
            if nM > self.M:
                continue
            if nC > self.C:
                continue
            if (nM != 0 and nM != self.M) and ((nC > nM) or ((self.C-nC) > (self.M-nM))):
                continue
            res.append(n[0])
        return res


if __name__ == "__main__":
    mc = MissCannibals(M=3, C=3)
    #print(mc.actions((3, 2, True)))
    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
