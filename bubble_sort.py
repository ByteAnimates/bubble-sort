# Bubble Sort — O(n²)
# As shown in the reel: https://www.facebook.com/reel/2011972776093831
# Generated from the episode; edits here are overwritten. See the README.

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
