import collections
import operator


def Find_minimum_visit(intervals):
    print(intervals)
    intervals.sort(key = operator.attrgetter("right"))
    print(intervals)
    num_visit = 0
    last_right = float("-inf")
    for input in intervals:
        if input.left > last_right:
            last_right = input.right
            num_visit += 1
    return num_visit


interval = collections.namedtuple("intervals", ("left", "right"))
intervals = [interval(1, 2), interval(2, 3), interval(3, 4), interval(2, 3), interval(3, 4), interval(4, 5)]
# interval2=list(map(interval,intervals))
# print(interval2)
print(Find_minimum_visit(intervals))
