from formalgrammar.utils import utils
import itertools
import functools
import operator


class Rule:
    def __init__(self, sym0, sym1):
        try:
            assert(iter(sym0))
            assert(iter(sym1))
        except TypeError:
            raise TypeError("Symbols have to be iterable")
        self.sym0 = sym0
        self.sym1 = sym1

    def inverse(self):
        return type(self)(self.sym1, self.sym0)


class Grammar:
    def __init__(self, rules, apply_all=False):
        self.rules = rules
        self.apply_all = apply_all

    def substitute(self, symbol):
        """
        Find all possible substituts for an arbitary
        symbol in respect to the predefined rules of
        a Grammar.
        """
        solutions = []
        for r in self.rules:
            if r.sym0 == symbol:
                solutions.append(r.sym1)
        if solutions:
            if self.apply_all is False:
                solutions.append(symbol)
            return tuple(solutions)
        else:
            return symbol,

    def create(self, state):
        length_state = len(state)
        maxtokensize = max(tuple(len(r.sym0) for r in self.rules))
        maxtokensize = min((maxtokensize, length_state))
        complete_solutions = []
        for tokensize in range(maxtokensize):
            zipped = zip(*[state[i:] for i in range(tokensize + 1)])
            solutions = [self.substitute(symbol) for symbol in zipped]
            complete_solutions.append(solutions)
        possible_partitions = utils.partition(list(range(length_state)))
        possible_partitions = utils.filter_subsets(possible_partitions,
                                                   maxtokensize + 1)
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
                operator.add, sol) for sol in possible_solutions)
            result.append(possible_solutions)
        return functools.reduce(operator.add, (tuple(gen) for gen in result))

    def mk_inverse_grammar(self):
        """
        Return a new Grammar - object, whose rules are upside down
        (left side goes to the right side and vice versa).
        """
        return type(self)([r.inverse() for r in self.rules])


class LSystem(Grammar):
    def __init__(self, rules):
        Grammar.__init__(self, rules, True)

    def walk(self, start):
        def generator(state):
            while True:
                yield state
                state = self.create(state)[0]
        return generator(start)

    def walk_to(self, start, depth, with_path=True):
        generator = self.walk()
        path = [next(generator) for i in range(depth)]
        if with_path is True:
            return path
        else:
            return path[-1]
