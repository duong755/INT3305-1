from typing import List


class PrefixCodeTree:
    def __init__(self):
        self.data: dict = {}

    def json(self):
        return self.data

    def insert(self, codeword: List[int], symbol: str) -> None:
        current_node: dict = self.data
        for bit in codeword:
            if bit == 0:
                if current_node.get("0") is None:
                    current_node.__setitem__("0", {})
                current_node = current_node.get("0")
            else:
                if current_node.get("1") is None:
                    current_node.__setitem__("1", {})
                current_node = current_node.get("1")
        current_node.__setitem__("leaf", symbol)

    def decode(self, encodedData: str, datalen: int) -> str:
        pass
