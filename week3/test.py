import json
from week3.prefixcodetree import PrefixCodeTree

codebook: dict = {
    "x1": [0],
    "x2": [1, 0, 0],
    "x3": [1, 0, 1],
    "x4": [1, 1]
}

codeTree = PrefixCodeTree()

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

print(json.dumps(codeTree.json(), indent=2, sort_keys=True))
print(codeTree.decode(b"\xd2\x9f\x20", 21))
