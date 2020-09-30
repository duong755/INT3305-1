import json
from week3.prefixcodetree import PrefixCodeTree

codebook: dict = {
    "x1": [0],
    "x2": [1, 0, 0],
    "x3": [1, 0, 1],
    "x4": [1, 1]
}

codeTree = PrefixCodeTree()

codeTree.insert([1, 0, 1], "a")
codeTree.insert([1, 1, 1], "b")
print(json.dumps(codeTree.json(), indent=2, sort_keys=True))
