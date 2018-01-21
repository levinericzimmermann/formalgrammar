from formalgrammar.grammar import grammar
import unittest


class TestPartition(unittest.TestCase):
    r0 = grammar.Rule(("a",), ("a", "b"))
    r1 = grammar.Rule(("b",), ("b",))
    r2 = grammar.Rule(("a", "b"), ("a", "a", "a"))
    r3 = grammar.Rule(("b",), ("a", "a"))
    r4 = grammar.Rule(("a", "b", "b"), ("a", "a"))

    TestGrammar0 = grammar.Grammar([r0, r1], apply_all=True)
    TestGrammar1 = grammar.Grammar([r0, r1, r2], apply_all=True)
    TestGrammar2 = grammar.Grammar([r0, r1, r3], apply_all=True)
    TestGrammar3 = grammar.Grammar([r0, r1, r2, r4], apply_all=True)
    TestGrammar4 = grammar.Grammar([r0, r1], apply_all=False)

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
        expected_result0 = (("a", "b"),)
        actual_result0 = tuple(self.TestGrammar0.create(("a",)))
        self.assertEqual(expected_result0, actual_result0)
        expected_result1 = (("a", "a", "a"), ("a", "b", "b"))
        actual_result1 = tuple(self.TestGrammar1.create(("a", "b")))
        self.assertEqual(expected_result1, actual_result1)
        expected_result2 = (("a", "b", "b"), ("a", "b", "a", "a"))
        actual_result2 = tuple(self.TestGrammar2.create(("a", "b")))
        self.assertEqual(expected_result2, actual_result2)
        expected_result3 = (("a", "a"), ("a", "b", "b", "b"),
                            ("a", "a", "a", "b"), ("a", "b", "b", "b"))
        actual_result3 = tuple(self.TestGrammar3.create(("a", "b", "b")))
        self.assertEqual(expected_result3, actual_result3)
        expected_result4 = (("a", "b"), ("a",))
        actual_result4 = tuple(self.TestGrammar4.create(("a",)))
        self.assertEqual(expected_result4, actual_result4)
