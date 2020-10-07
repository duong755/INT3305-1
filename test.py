import json
from prefixcodetree import PrefixCodeTree

codebook: dict = {
    "x1": [0],
    "x2": [1, 0, 0],
    "x3": [1, 0, 1],
    "x4": [1, 1]
}

codeTree = PrefixCodeTree()

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

try:
    json_string = json.dumps(codeTree.root, indent=2, sort_keys=True)
    print(json_string)

    print(codeTree.decode(b"\xd2\x9f\x20", 21))
except TypeError:
    print("String is not decodable")
