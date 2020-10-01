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

try:
    json_string = json.dumps(codeTree.json(), indent=2, sort_keys=True)
    print(json_string)

    bits, symbols = codeTree.decode(b"\xd2\x9f\x20", 21)
    for bit in bits:
        print(str(bit).ljust(4, ' '), end="")

    print()
    for symbol in symbols:
        print(symbol.ljust(4, ' '), end="")
except TypeError:
    print("String is not decodable")
