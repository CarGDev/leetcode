# Linked List Cycle

[![Problem 141](https://img.shields.io/badge/Problem-141-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/linked-list-cycle/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/linked-list-cycle/)

**Problem Number:** [141](https://leetcode.com/problems/linked-list-cycle/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, Linked List, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/linked-list-cycle/](https://leetcode.com/problems/linked-list-cycle/)

## Problem Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3:**
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

**Constraints:**
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

## My Approach

I used **Floyd's Cycle-Finding Algorithm (Tortoise and Hare)** with two pointers. The key insight is that if there's a cycle, a fast pointer will eventually catch up to a slow pointer.

**Algorithm:**
1. Initialize two pointers (slow and fast) at the head
2. Move slow pointer by one step and fast pointer by two steps
3. If fast pointer reaches null, there's no cycle
4. If slow and fast pointers meet, there's a cycle
5. Return true if cycle detected, false otherwise

## Solution

The solution uses Floyd's cycle-finding algorithm with two pointers. See the implementation in the [solution file](../exercises/141.linked-list-cycle.py).

**Key Points:**
- Uses two pointers moving at different speeds
- Slow pointer moves one step at a time
- Fast pointer moves two steps at a time
- Detects cycle when pointers meet
- Handles null pointers properly

## Time & Space Complexity

**Time Complexity:** O(n)
- In worst case, fast pointer traverses the list twice
- Each pointer moves at most n steps
- Total: O(n)

**Space Complexity:** O(1)
- Uses only two pointers
- No additional data structures
- Constant extra space

## Key Insights

1. **Floyd's Algorithm:** Using two pointers at different speeds is the most efficient way to detect cycles.

2. **Mathematical Proof:** If there's a cycle, the fast pointer will eventually catch up to the slow pointer.

3. **No Extra Space:** This approach doesn't require storing visited nodes.

4. **Linear Time:** The algorithm runs in linear time regardless of cycle length.

5. **Null Handling:** Properly handles cases where the list ends without a cycle.

6. **Pointer Meeting:** When pointers meet, it indicates a cycle exists.

## Mistakes Made

1. **Hash Set Approach:** Initially might use hash set to track visited nodes, requiring O(n) space.

2. **Wrong Speeds:** Not using the correct speed ratio (1:2) for the pointers.

3. **Null Checks:** Not properly handling null pointer cases.

4. **Complex Logic:** Overcomplicating the cycle detection logic.

## Related Problems

- **Linked List Cycle II** (Problem 142): Find the node where cycle begins
- **Happy Number** (Problem 202): Cycle detection in number sequence
- **Find the Duplicate Number** (Problem 287): Cycle detection in array
- **Palindrome Linked List** (Problem 234): Check if linked list is palindrome

## Alternative Approaches

1. **Hash Set:** Store visited nodes in hash set - O(n) time, O(n) space
2. **Marking Nodes:** Mark visited nodes by changing their values - O(n) time, O(1) space
3. **Recursive:** Use recursion with visited tracking - O(n) time, O(n) space

## Common Pitfalls

1. **Hash Set Usage:** Using hash set when two pointers are more efficient.
2. **Wrong Speeds:** Not using the correct 1:2 speed ratio for pointers.
3. **Null Handling:** Not properly checking for null pointers.
4. **Complex Implementation:** Overcomplicating the cycle detection.
5. **Space Inefficiency:** Using O(n) space when O(1) is possible.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/141.linked-list-cycle.py)](../exercises/141.linked-list-cycle.py)

*Note: This is a classic two-pointer problem that demonstrates efficient cycle detection with Floyd's algorithm.*
