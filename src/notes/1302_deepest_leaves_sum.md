# Deepest Leaves Sum

[![Problem 1302](https://img.shields.io/badge/Problem-1302-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/deepest-leaves-sum/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/deepest-leaves-sum/)

**Problem Number:** [1302](https://leetcode.com/problems/deepest-leaves-sum/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**LeetCode Link:** [https://leetcode.com/problems/deepest-leaves-sum/](https://leetcode.com/problems/deepest-leaves-sum/)

## Problem Description

Given the `root` of a binary tree, return the sum of values of its deepest leaves.

**Example 1:**
```
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Explanation: The deepest leaves are the nodes with values 7 and 8 respectively.
The sum of their values is 7 + 8 = 15.
```

**Example 2:**
```
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
```

**Constraints:**
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `1 <= Node.val <= 100`

## My Approach

I used a **Depth-First Search (DFS)** approach with depth tracking. The key insight is to traverse the tree and keep track of the maximum depth found, then sum all leaf nodes at that maximum depth.

**Algorithm:**
1. Initialize maximum depth and sum variables
2. Use DFS to traverse the tree recursively
3. For each leaf node, check if it's at the deepest level
4. If current depth is greater than maximum depth, update maximum depth and reset sum
5. If current depth equals maximum depth, add leaf value to sum
6. Recursively traverse left and right children
7. Return the sum of deepest leaves

## Solution

The solution uses DFS with depth tracking to find the sum of deepest leaves. See the implementation in the [solution file](../exercises/1302.deepest-leaves-sum.py).

**Key Points:**
- Uses recursive DFS to traverse the tree
- Tracks maximum depth found so far
- Resets sum when deeper level is found
- Accumulates sum for leaves at maximum depth
- Handles leaf nodes (nodes with no children)
- Returns sum of all deepest leaves

## Time & Space Complexity

**Time Complexity:** O(n)
- DFS visits each node exactly once
- Each node operation is constant time
- Total: O(n)

**Space Complexity:** O(h)
- h is the height of the tree
- Recursion stack space
- In worst case (skewed tree): O(n)
- In best case (balanced tree): O(log n)

## Key Insights

1. **DFS Traversal:** Using DFS allows us to explore the tree and find the deepest level.

2. **Depth Tracking:** We need to track the maximum depth to identify the deepest leaves.

3. **Leaf Detection:** A leaf node is identified when it has no left and right children.

4. **Sum Accumulation:** When we find leaves at the maximum depth, we accumulate their values.

5. **Depth Reset:** When we find a deeper level, we reset the sum and update the maximum depth.

6. **Recursive Structure:** The tree structure naturally lends itself to recursive traversal.

## Mistakes Made

1. **Wrong Traversal:** Initially might use BFS when DFS is more appropriate for depth tracking.

2. **Complex Logic:** Overcomplicating the depth tracking with unnecessary data structures.

3. **Wrong Leaf Detection:** Not properly identifying leaf nodes.

4. **Sum Logic:** Not correctly handling the case when deeper levels are found.

## Related Problems

- **Maximum Depth of Binary Tree** (Problem 104): Find maximum depth of binary tree
- **Binary Tree Level Order Traversal** (Problem 102): Level-by-level traversal
- **Sum Root to Leaf Numbers** (Problem 129): Sum of all root-to-leaf paths
- **Path Sum** (Problem 112): Check if path sum equals target

## Alternative Approaches

1. **Breadth-First Search:** Use BFS with level tracking - O(n) time, O(w) space
2. **Two Pass DFS:** First pass to find max depth, second pass to sum leaves - O(n) time
3. **Iterative DFS:** Use stack for iterative DFS - O(n) time, O(h) space

## Common Pitfalls

1. **Wrong Traversal:** Using BFS when DFS is more suitable for depth tracking.
2. **Complex Implementation:** Overcomplicating the depth tracking logic.
3. **Wrong Leaf Detection:** Not properly identifying leaf nodes.
4. **Sum Logic Errors:** Not correctly handling depth updates and sum resets.
5. **Space Complexity:** Not considering recursion stack space.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/1302.deepest-leaves-sum.py)](../exercises/1302.deepest-leaves-sum.py)

*Note: This is a tree traversal problem that demonstrates efficient depth tracking with DFS.*
