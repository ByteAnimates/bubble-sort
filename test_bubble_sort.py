"""
Run it: python3 test_bubble_sort.py   (or: pytest)

Plain asserts, no dependencies. Properties of the algorithm rather than snapshots of its
output, so they stay true if you rewrite the internals.
"""

from bubble_sort import bubble_sort
from main import VALUES, passes


def test_it_sorts_and_returns_nothing():
    # The snippet has no `return` — it sorts the list it was handed and hands back None.
    a = list(VALUES)
    assert bubble_sort(a) is None
    assert a == sorted(VALUES)


def test_sorted_input_costs_exactly_one_pass():
    # The claim the episode is about. The first pass swaps nothing, `swapped` stays
    # False, and the loop breaks — which is the line most implementations leave out.
    assert passes(sorted(VALUES))[0] == 1
    assert passes([2, 1])[0] == 1
    assert passes([1])[0] == 0


def test_shuffled_input_costs_more_than_one_pass():
    # If this ever failed, the early exit would be firing when it should not.
    assert passes(VALUES)[0] > 1


def test_worst_case_is_n_minus_one_passes():
    # A reversed array never gives the early exit a chance.
    rev = sorted(VALUES, reverse=True)
    assert passes(rev)[0] == len(rev) - 1


def test_each_pass_settles_one_more_value_at_the_end():
    rev = sorted(VALUES, reverse=True)
    _, frames = passes(rev)
    for i, row in enumerate(frames, 1):
        assert row[len(rev) - i:] == sorted(rev)[len(rev) - i:]


def test_edge_cases():
    for case in ([], [1], [3, 3, 3], [2, 1], VALUES, sorted(VALUES, reverse=True)):
        a = list(case)
        bubble_sort(a)
        assert a == sorted(case)


if __name__ == '__main__':
    passed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
            passed += 1
    print(f'\n{passed} tests passed\n')
