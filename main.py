"""
Run it: python3 main.py

The reel's claim is the early exit: a pass that swaps nothing means the array is already
sorted, so the loop can stop. It is the line most implementations leave out, and without
it bubble sort cannot tell a sorted array from a shuffled one.
"""

from bubble_sort import bubble_sort

VALUES = [24, 11, 45, 18, 63]   # the five the reel sorts


def passes(a: list[int]) -> tuple[int, list[list[int]]]:
    """
    `(passes, frames)` — the same loop, recording the array after each pass.

    An instrumented copy rather than a wrapper, because the number worth seeing is how
    many times the outer loop runs, and that is invisible from outside the function.
    """
    a = list(a)
    frames = []
    n = len(a)
    runs = 0
    for i in range(n - 1):
        runs += 1
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        frames.append(list(a))
        if not swapped:
            break
    return runs, frames


def main() -> None:
    runs, frames = passes(VALUES)

    print(f'\n{VALUES}\n')
    for i, row in enumerate(frames, 1):
        # Everything from the boundary rightwards is settled: each pass floats one more
        # value into its final place at the end.
        settled = len(frames[0]) - i
        head = '  '.join(f'{v:>2}' for v in row[:settled])
        tail = '  '.join(f'{v:>2}' for v in row[settled:])
        print(f'  pass {i}  [{head} | {tail}]')

    print(f'\n  sorted in {runs} passes\n')

    for name, data in (('shuffled', VALUES), ('already sorted', sorted(VALUES))):
        print(f'  {name:<16} {passes(data)[0]} pass{"es" if passes(data)[0] != 1 else ""}')

    print(
        '\n  One pass on sorted input, and it is the early exit that does it: the pass\n'
        '  swaps nothing, `swapped` stays False, and the loop breaks. Take that line out\n'
        '  and bubble sort walks the whole array four times to discover the same thing.\n'
    )


# ── the claims above, checked ────────────────────────────────────────────────────

# It sorts, in place, and returns nothing — the snippet has no `return`.
_a = list(VALUES)
assert bubble_sort(_a) is None
assert _a == sorted(VALUES)

# THE CLAIM: sorted input costs exactly one pass, because the first pass swaps nothing.
assert passes(sorted(VALUES))[0] == 1
assert passes([1])[0] == 0
assert passes([2, 1])[0] == 1

# And a shuffled array costs more than one, or the early exit would be firing wrongly.
assert passes(VALUES)[0] > 1

# Worst case is n-1 passes: the early exit never gets a chance on a reversed array.
_rev = sorted(VALUES, reverse=True)
assert passes(_rev)[0] == len(_rev) - 1

# Every pass floats one more value to the end for good.
_, _frames = passes(_rev)
for _i, _row in enumerate(_frames, 1):
    assert _row[len(_rev) - _i:] == sorted(_rev)[len(_rev) - _i:]

for _case in ([], [1], [3, 3, 3], [2, 1], VALUES, _rev):
    _c = list(_case)
    bubble_sort(_c)
    assert _c == sorted(_case)

if __name__ == '__main__':
    main()
