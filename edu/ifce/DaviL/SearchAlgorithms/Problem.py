from abc import abstractmethod
from random import choice, shuffle
from numpy import zeros


class Problem(object):
    """
        Abstract class
    """
    goal = None  # type: object

    def __init__(self, initial_state, goal=None):
        super(Problem, self).__init__()
        self.initial_state = initial_state
        self.goal = goal

    @abstractmethod
    def actions(self, state):
        return NotImplementedError

    @abstractmethod
    def result(self, state, action):
        return NotImplementedError

    def test_goal(self, state):
        return state == self.goal

    @abstractmethod
    def get_goal(self):
        return self.goal


class RomeniaProblem(Problem):
    def __init__(self, initial_state, goal):
        # type: () -> object
        super(Problem, self).__init__()
        self.initial_state = initial_state
        self.goal = goal

    def actions(self, state):

        '''

        :param state:
        :return: the actions of a state

        '''
        actions = {
            'arad': {'zerind': 75, 'sibiu': 140, 'timisoara': 118},
            'zerind': {'arad': 75, 'oradea': 71},
            'timisoara': {'arad': 118, 'lugoj': 111},
            'bucharest': {'urziceni': 85, 'pitesti': 101, 'giurgiu': 90, 'fagaras': 211},
            'craiovoa': {'drobeta': 120, 'rimmicu vilcea': 146, 'pitesti': 138},
            'drobeta': {'mehadia': 75, 'craiovoa': 120},
            'eforie': {'hirsova': 86},
            'fagaras': {'sibiu': 99, 'bucharest': 211},
            'hirsova': {'urziceni': 98, 'eforie': 86},
            'iasi': {'vaslui': 92, 'neamt': 87},
            'lugoj': {'timisoara': 111, 'mehadia': 70},
            'oradea': {'zerind': 71, 'sibiu': 151},
            'pitesti': {'rimmicu vilcea': 97, 'craiovoa': 138, 'bucharest': 101},
            'urziceni': {'vaslui': 142, 'bucharest': 85, 'hirsova': 98},
            'neamt': {'iasi': 87},
            'vaslui': {'iasi': 92, 'urziceni': 142},
            'giurgiu': {'bucharest': 90},
            'rimmicu vilcea': {'sibiu': 99, 'pitesti': 97, 'craiovoa': 146},
            'sibiu': {'fagaras': 99, 'rimmicu vilcea': 80, 'arad': 140, 'oradea': 151},
            'mehadia': {'lugoj': 70, 'drobeta': 75}
        }
        shuffle(actions[state].keys())
        print actions[state]
        return actions[state]

    def result(self, state, action):
        """

        :param state:
        :param action:
        :return:  Result in a new state of the problem given an action

        """

        if action is not None:
            actions = self.actions(state)
            next_state, value = choice(list(actions.items()))
            return next_state
        return state

    def get_goal(self):
        return self.goal

    def execution(self, path):
        for next_action in range(len(path) - 1):
            print 'Estado atual %s ir para %s' % (path[next_action], path[next_action + 1])

        print 'Chegou em %s' % (path[len(path) - 1])
