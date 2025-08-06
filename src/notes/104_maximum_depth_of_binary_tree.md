# Maximum Depth of Binary Tree

[![Problem 104](https://img.shields.io/badge/Problem-104-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**Problem Number:** [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**LeetCode Link:** [https://leetcode.com/problems/maximum-depth-of-binary-tree/](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Problem Description

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**
```
Input: root = [1,null,2]
Output: 2
```

**Constraints:**
- The number of nodes in the tree is in the range `[0, 10^4]`
- `-100 <= Node.val <= 100`

## My Approach

I used a **Recursive Depth-First Search** approach. The key insight is to recursively calculate the depth of left and right subtrees and return the maximum depth plus one for the current node.

**Algorithm:**
1. Handle base case: if root is None, return 0
2. Use a recursive helper function that tracks current depth
3. Recursively calculate depth of left and right subtrees
4. Return the maximum of left and right depths plus 1 for current node
5. The final result is the maximum depth of the entire tree

## Solution

The solution uses recursive DFS to find the maximum depth. See the implementation in the [solution file](../exercises/104.maximum-depth-of-binary-tree.py).

**Key Points:**
- Uses recursive DFS to traverse the tree
- Handles null nodes by returning 0
- Tracks current depth and finds maximum
- Returns maximum depth of left and right subtrees
- Adds 1 for the current node level

## Time & Space Complexity

**Time Complexity:** O(n)
- We visit each node exactly once
- Each node operation is O(1)
- Total: O(n) where n is the number of nodes

**Space Complexity:** O(h)
- Recursion stack depth equals tree height
- In worst case (skewed tree): O(n)
- In best case (balanced tree): O(log n)

## Key Insights

1. **Recursive DFS:** Using recursion provides a clean and intuitive solution for tree traversal.

2. **Base Case:** Null nodes have depth 0, providing a clear termination condition.

3. **Maximum Depth:** We take the maximum of left and right subtree depths since we want the longest path.

4. **Depth Calculation:** Each level adds 1 to the depth, so we add 1 to the maximum subtree depth.

5. **Tree Properties:** The maximum depth is the length of the longest path from root to leaf.

6. **Efficient Traversal:** DFS visits each node only once, making it efficient.

## Mistakes Made

1. **Wrong Base Case:** Initially might not handle null nodes properly.

2. **Complex Logic:** Overcomplicating the depth calculation with unnecessary variables.

3. **Wrong Return Value:** Not adding 1 for the current node level.

4. **Inefficient Approach:** Using BFS when DFS is simpler and more efficient.

## Related Problems

- **Minimum Depth of Binary Tree** (Problem 111): Find minimum depth
- **Balanced Binary Tree** (Problem 110): Check if tree is balanced
- **Binary Tree Level Order Traversal** (Problem 102): Level-by-level traversal
- **Symmetric Tree** (Problem 101): Check if tree is symmetric

## Alternative Approaches

1. **Iterative DFS:** Use stack for iterative depth-first search - O(n) time, O(h) space
2. **BFS:** Use queue for breadth-first search - O(n) time, O(w) space where w is max width
3. **Level Order Traversal:** Count levels using BFS approach

## Common Pitfalls

1. **Wrong Base Case:** Not handling null nodes correctly.
2. **Complex Implementation:** Overcomplicating the recursive logic.
3. **Wrong Depth Calculation:** Not adding 1 for the current node.
4. **Inefficient Approach:** Using BFS when DFS is simpler.
5. **Stack Overflow:** Not considering very deep trees for recursion.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/104.maximum-depth-of-binary-tree.py)](../exercises/104.maximum-depth-of-binary-tree.py)

*Note: This is a fundamental tree traversal problem that demonstrates efficient use of recursive DFS.*
