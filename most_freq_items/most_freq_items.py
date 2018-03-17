from collections import Counter

text = "Recursive solutions are often easier to read and write for branching problems. Tree traversals, graph "\
        "traversals, and mathematical series are (often) dealt with more intuitively using recursion."\

"Though it affords convenience, the computational time cost of recursion on" \
"branching problems grows exponentially with larger values of n."
words = text.split()
counter = Counter(words)
# for top three occurring
counter_common = counter.most_common(3)
print(words)
print(counter)
print(counter_common)