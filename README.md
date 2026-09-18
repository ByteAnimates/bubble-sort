# Bubble Sort

**O(n²)** · [Watch the reel](https://www.facebook.com/reel/2011972776093831)

The working code from the [@ByteAnimates](https://www.facebook.com/ByteAnimates) reel.

```bash
python3 main.py
python3 bubble_sort.py
python3 test_bubble_sort.py
```

No dependencies. Python 3.9+.

### `bubble_sort.py`

```python
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
                swapped = True
        if not swapped:
            break
```

### Files

| | |
| --- | --- |
| `bubble_sort.py` | the reel snippet, generated from the episode |
| `main.py` | run this — the demo, with real inputs and real output |
| `test_bubble_sort.py` | the properties, checked — they survive a rewrite |

---

The snippet above is generated from the video itself — what you read is byte-for-byte
what was typed on screen. A fix to it belongs in the episode, so open an issue and the
next reel carries it. Everything else here is hand-written and welcome as a pull request.
