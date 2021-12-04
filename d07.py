from collections import defaultdict
from typing import List


def parse(input: List[str]):
    forwards = defaultdict(list)
    backwards = defaultdict(list)
    for line in input:
        start = line[5]
        end = line[36]
        forwards[start].append(end)
        backwards[end].append(start)
    for v in forwards.values():
        v.sort()
    for v in backwards.values():
        v.sort()

    return forwards, backwards


def find_ends(forwards, backwards):
    starts = set(forwards.keys())
    ends = set(backwards.keys())
    front = starts - ends
    back = ends - starts
    # assert len(front) == 1
    assert len(back) == 1
    return sorted(list(front)), back.pop()


def p1(input: List[str]):
    forwards, backwards = parse(input)
    front, back = find_ends(forwards, backwards)
    current = front[0]
    res = current
    attempts = front[1:]
    while current != back:
        for node in forwards[current]:
            if node not in attempts:
                attempts.append(node)
        attempts.sort()
        # if all(prev in res for prev in backwards[current]):
        current = next(node for node in attempts if all(
            prev in res for prev in backwards[node]))
        attempts.remove(current)
        res += current
    return res


sample = ["Step C must be finished before step A can begin.",
          "Step C must be finished before step F can begin.",
          "Step A must be finished before step B can begin.",
          "Step A must be finished before step D can begin.",
          "Step B must be finished before step E can begin.",
          "Step D must be finished before step E can begin.",
          "Step F must be finished before step E can begin."]
assert p1(sample) == "CABDFE"

lines = open("d07.txt", 'r').readlines()
assert p1(lines) == "GJFMDHNBCIVTUWEQYALSPXZORK"

