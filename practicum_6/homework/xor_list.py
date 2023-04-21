from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import ctypes

import yaml


@dataclass
class Element:
    key: Any
    data: Any = None
    np: int = 0

    def next(self, prev_np) -> int:
        next_np = self.np ^ prev_np
        return next_np


    def prev(self, next_np) -> int:
        prev_np = self.np ^ next_np
        return prev_np


class XorDoublyLinkedList:
    def __init__(self) -> None:
        self.head: Element = None
        self.tail: Element = None
        self.nodes = []


    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        nodes = []
        node = self.head
        prev_np = 0

        while node:
            nodes.append(str(node.key))
            next_np = prev_np ^ node.np
            if next_np:
                prev_np = id(node)
                node = ctypes.cast(next_np, ctypes.py_object).value
            else:
                break
        return " <-> ".join(nodes)

    def to_pylist(self) -> list[Any]:
        py_list = []
        node = self.head
        prev_np = 0

        while node:
            py_list.append(node.key)
            next_np = prev_np ^ node.np
            if next_np:
                prev_np = id(node)
                node = ctypes.cast(next_np, ctypes.py_object).value
            else:
                break
        return py_list

    def empty(self):
        return self.head is None

    def search(self, k: Element) -> Element:
        """Complexity: O(n)"""
        if self.empty():
            return "This list is empty"

        next_np = id(self.head)
        prev_np = 0
        next_element = self.head

        while next_np != 0 and next_element.key != k.key:
            prev_np, next_np = next_np, next_element.next(prev_np)
            if next_id == 0:
                return "This list doesn't store this element"
            next_element = ctypes.cast(next_np, ctypes.py_object).value
        return next_element

    def insert(self, x: Element) -> None:
        """Insert to the front of the list (i.e., it is 'prepend')
        Complexity: O(1)
        """
        if self.empty():
            self.head = self.tail = x
        else:
            x.np = id(self.head)
            self.head.np = self.head.np ^ id(x)
            self.head = x
        self.nodes.append(x)

    def remove(self, x: Element) -> None:
        """Remove x from the list
        Complexity: O(1)
        """
        if self.empty():
            return

        if not x:
            return

        next_np = id(self.head)
        prev_np = 0
        next_element = ctypes.cast(next_np, ctypes.py_object).value
        while next_np != 0 and next_element.key != x.key:
            prev_np, next_np = next_np, next_element.next(prev_np)
            next_element = ctypes.cast(next_np, ctypes.py_object).value
        if next_np != 0:
            next_next_np = next_element.np ^ prev_np
            if prev_np != 0:
                prev_element = ctypes.cast(prev_np, ctypes.py_object).value
                prev_element.np = prev_element.np ^ next_np ^ next_next_np
            else:
                self.head = next_next_element
            if next_next_np != 0:
                next_next_element = ctypes.cast(next_next_np, ctypes.py_object).value
                next_next_element.np = next_next_element.np ^ next_np ^ prev_np
            else:
                self.tail = prev_element
            self.nodes.remove(next_element)


    def reverse(self) -> XorDoublyLinkedList:
        """Returns the same list but in the reserved order
        Complexity: O(1)
        """
        self.head, self.tail = self.tail, self.head
        return self


if __name__ == "__main__":
    # You need to implement a doubly linked list using only one pointer
    # self.np per element. In python, by pointer, we understand id(object).
    # Any object can be accessed via its id, e.g.
    # >>> import ctypes
    # >>> a = ...
    # >>> ctypes.cast(id(a), ctypes.py_object).value
    # Hint: assuming that self.next and self.prev store pointers
    # define self.np as self.np = self.next XOR self.prev
    with open("xor_list_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        l = XorDoublyLinkedList()
        for el in reversed(c["input"]["list"]):
            l.insert(Element(key=el))
        print(l)
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                l.insert(Element(key=op_info["key"]))
                print(l)
            elif op_info["op"] == "remove":
                l.remove(Element(op_info["key"]))
                print(l)
            elif op_info["op"] == "reverse":
                l = l.reverse()
                print(l)
        py_list = l.to_pylist()
        print(py_list)
        print(f"Case #{i + 1}: {py_list == c['output']}")