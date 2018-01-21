from formalgrammar import grammar
import unittest


class TestPartition(unittest.TestCase):
    r0 = grammar.Rule(("a",), ("a", "b"))
    r1 = grammar.Rule(("b",), ("b",))
    r2 = grammar.Rule(("a", "b"), ("a", "a", "a"))
    r3 = grammar.Rule(("b",), ("a", "a"))

    TestGrammar0 = grammar.Grammar([r0, r1])
    TestGrammar1 = grammar.Grammar([r0, r1, r2])
    TestGrammar2 = grammar.Grammar([r0, r1, r3])

    def test_substitute(self):
        possible_solutions0 = self.TestGrammar0.substitute(("a",))
        self.assertEqual(possible_solutions0, (("a", "b"),))
        possible_solutions1 = self.TestGrammar0.substitute(("b",))
        self.assertEqual(possible_solutions1, (("b",),))
        possible_solutions2 = self.TestGrammar1.substitute(("a", "b",))
        self.assertEqual(possible_solutions2, (("a", "a", "a"),))
        possible_solutions3 = self.TestGrammar2.substitute(("b",))
        self.assertEqual(possible_solutions3, (("b",), ("a", "a")))

    def test_create(self):
        pass
