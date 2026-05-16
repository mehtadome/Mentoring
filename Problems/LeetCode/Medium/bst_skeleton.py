from __future__ import annotations
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, determine if it is a valid BST under the following rule:
            - Left subtree values must be strictly less than the node (<)
            - Right subtree values must be greater than or equal to the node (>=)
        This rule applies recursively to every node in the tree.
        Trees are given as level-order arrays; None indicates a missing node.

        Example 1:
            tree = [4, 2, 6]
                4
               / \
              2   6
            Output: True

        Example 2:
            tree = [4, 2, 4]
                4
               / \
              2   4   <- duplicate 4 is allowed in the right subtree
            Output: True
        """
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([4, 2, 6],                        True),
        ([4, 2, 4],                        True),
        ([4, 4, 6],                        False),
        ([5, 1, 7, None, None, 3, None],   False),
        ([1],                              True),
        ([4, None, 4, None, 4],            True),
        ([4, None, 4, 3, None],            False),
        ([5, 1, 7, None, None, 5, 8],      True),
    ]

    passed = 0
    for values, expected in tests:
        try:
            root = build(values)
            result = sol.isValidBST(root)
            status = "PASS" if result == expected else "FAIL"
            if status == "PASS":
                passed += 1
            print(f"{status}  tree={values}  expected={expected}, got={result}")
        except NotImplementedError:
            print(f"SKIP  tree={values}  (not implemented)")

    print(f"\n{passed}/{len(tests)} passed")
