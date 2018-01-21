import functools
import operator


def partition(collection):
    """
    https://stackoverflow.com/questions/19368375/set-partitions-in-python
    """
    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n + 1:]
        # put `first` in its own subset
        yield [[first]] + smaller


def filter_subsets(partitions, border):
    def test(partition):
        return all(tuple(len(sub) < border for sub in partition))
    return filter(test, partitions)


def filter_unordered_subsets(partitions):
    def test(partition):
        reduced = functools.reduce(operator.add, partition)
        return list(reduced) == sorted(reduced)
    return filter(test, partitions)
