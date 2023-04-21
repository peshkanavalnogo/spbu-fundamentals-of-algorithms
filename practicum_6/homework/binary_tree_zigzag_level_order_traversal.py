from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from queue import *
from collections import *

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self, root) -> list[Any]:
        if not root: return []
        ans = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth % 2 == 0:
                ans[depth].append(node.key)
            else:
                ans[depth].insert(0, node.key)
            if node.left: queue.append((node.left, depth + 1))
            if node.right: queue.append((node.right, depth + 1))
        return list(ans.values())

def build_tree(list_view: list[Any]) -> BinaryTree:
    bt = BinaryTree()
    if list_view:
        node = Node(key=list_view[0])
        bt.root = node

        nodes = [node]
        for i, x in enumerate(list_view[1:]):
            if x is None:
                continue
            parent = nodes[i // 2]
            new_node = Node(key=x)
            new_node.key = x
            if i % 2 == 0:
                parent.left = new_node
            else:
                parent.right = new_node
            nodes.append(new_node)
    else:
        bt.root = None

    return bt



if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open("binary_tree_zigzag_level_order_traversal_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal(bt.root)
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
