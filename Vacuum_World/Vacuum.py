# Vacuum.py

import importlib as il

import numpy as np
import Environs
import Agency
il.reload(Environs)
il.reload(Agency)


def f_scoring(scores, agents, state):
    for i, agent in enumerate(agents):
        if agent.action != 'powerdown':
            scores[i] -= 1
        if agent.action == 'suck' and state[agent.loc[0], agent.loc[1]] == 1:
            scores[i] += 100
        if agent.action == 'powerdown' and (agent.loc-agent.home_loc).sum()!=0:
            scores[i] -= 1000
    return scores


def f_homeless(scores, agents, state):
    for i, agent in enumerate(agents):
        if agent.action != 'powerdown':
            scores[i] -= 1
        if agent.action == 'suck' and state[agent.loc[0], agent.loc[1]] == 1:
            scores[i] += 100
    return scores

def f_action(agents, state):
    for agent in agents:
        if agent.action == 'suck':
            state[agent.loc[0], agent.loc[1]] = 0
        elif (agent.action == 'move'
                and min(agent.loc + agent.bearing) >= 0
                and min(state.shape - agent.loc - agent.bearing) > 0
                and state[agent.loc[0] + agent.bearing[0],
                            agent.loc[1] + agent.bearing[1]] != 2):
            agent.loc += agent.bearing
        elif agent.action == 'rturn':
            agent.bearing = [agent.bearing[1], -agent.bearing[0]]
        elif agent.action == 'lturn':
            agent.bearing = [-agent.bearing[1], agent.bearing[0]]
    return state

def run_eval_environment(state, update, agents, performance):
    scores = [0 for _ in range(len(agents))]
    while any([agent.action != 'powerdown' for agent in agents]):
        for agent in agents:
            agent.get_percept(state)
            agent.program()
        scores = performance(scores, agents, state)
        state = update(agents, state)
    return scores

'''
for S in Environs.MiniMax2Package():
    agents = [Agency.TrivialTableLookupAgent(np.array([0,0]), np.array([0,0]), 'E')]
    print run_eval_environment(S.grid, f_action, agents, f_scoring)
'''

agents = [Agency.EmptyRoomInternalStateReflexAgent(np.array([0,0]), np.array([0,0]), 'E')]
print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
