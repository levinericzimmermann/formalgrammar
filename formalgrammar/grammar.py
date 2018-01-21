from formalgrammar.utils import utils
import itertools
import functools


class Grammar:
    apply_all = False  # currenlty applied to all (all symbols
    # which could be solved get solved)

    def __init__(self, rules):
        self.rules = rules

    def substitute(self, symbol):
        """
        Find all possible substituts for an arbitary
        symbol in respect to the defined rules of
        a Grammar.
        """
        solutions = []
        for r in self.rules:
            if r.sym0 == symbol:
                solutions.append(r.sym1)
        if solutions:
            return tuple(solutions)
        else:
            return symbol

    def create(self, state):
        length_state = len(state)
        highest_context = max(tuple(len(r.sym0) for r in self.rules))
        max_context = min((highest_context, length_state))
        complete_solutions = []
        for tokensize in range(max_context):
            solutions = []
            zipped = zip(*[state[i:] for i in range(tokensize + 1)])
            for symbol in zipped:
                sol = self.substitute(symbol)
                solutions.append(sol)
            complete_solutions.append(solutions)
        possible_partitions = utils.partition(list(range(length_state)))
        possible_partitions = utils.filter_subsets(possible_partitions,
                                                   max_context + 1)
        possible_partitions = utils.filter_unordered_subsets(
                possible_partitions)
        result = []
        for part in possible_partitions:
            solutions = []
            for sub in part:
                ind0 = len(sub) - 1
                ind1 = sub[0]
                sol = complete_solutions[ind0][ind1]
                solutions.append(sol)
            possible_solutions = itertools.product(*solutions)
            possible_solutions = (functools.reduce(
                lambda x, y: x + y, sol) for sol in possible_solutions)
            result.append(possible_solutions)
        return result


class Rule:
    def __init__(self, sym0, sym1):
        try:
            assert(iter(sym0))
        except TypeError:
            raise TypeError("Symbols may be iterables")
        try:
            assert(iter(sym1))
        except TypeError:
            raise TypeError("Symbols may be iterables")
        self.sym0 = sym0
        self.sym1 = sym1

    def inverse(self):
        return type(self)(self.sym1, self.sym0)
