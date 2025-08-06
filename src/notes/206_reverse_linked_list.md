# Reverse Linked List

[![Problem 206](https://img.shields.io/badge/Problem-206-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/reverse-linked-list/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/reverse-linked-list/)

**Problem Number:** [206](https://leetcode.com/problems/reverse-linked-list/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Linked List, Recursion
**LeetCode Link:** [https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reverse-linked-list/)

## Problem Description

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**
```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**
```
Input: head = []
Output: []
```

**Constraints:**
- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both solutions?

## My Approach

I used an **Iterative** approach with three pointers to reverse the linked list. The key insight is to use three pointers (prev, curr, next) to reverse the links one by one.

**Algorithm:**
1. Initialize prev to None and curr to head
2. While curr is not None:
   - Store next node (curr.next)
   - Reverse the link (curr.next = prev)
   - Move prev to curr
   - Move curr to next
3. Return prev (new head)

## Solution

The solution uses iterative approach with three pointers to reverse the linked list. See the implementation in the [solution file](../exercises/206.reverse-linked-list.py).

**Key Points:**
- Uses three pointers: prev, curr, next
- Reverses links one by one
- Handles empty list case
- Returns new head (prev)
- Simple and efficient approach

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through the linked list
- Each node is visited once
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Three Pointers:** Using prev, curr, and next pointers simplifies the reversal.

2. **Link Reversal:** Each iteration reverses one link: curr.next = prev.

3. **Pointer Movement:** Moving pointers in the correct order is crucial.

4. **New Head:** The new head is the last node (prev after loop ends).

5. **Empty List:** Handles empty list case naturally.

6. **Single Node:** Works correctly for single node lists.

## Mistakes Made

1. **Wrong Pointer Order:** Initially might move pointers in wrong order.

2. **Lost References:** Not storing next node before changing curr.next.

3. **Complex Logic:** Overcomplicating the pointer manipulation.

4. **Wrong Return:** Returning wrong pointer as new head.

## Related Problems

- **Reverse Linked List II** (Problem 92): Reverse portion of linked list
- **Palindrome Linked List** (Problem 234): Check if linked list is palindrome
- **Add Two Numbers** (Problem 2): Add numbers represented by linked lists
- **Merge Two Sorted Lists** (Problem 21): Merge sorted linked lists

## Alternative Approaches

1. **Recursive:** Use recursion to reverse list - O(n) time, O(n) space
2. **Stack-based:** Use stack to reverse order - O(n) time, O(n) space
3. **Array-based:** Convert to array, reverse, rebuild - O(n) time, O(n) space

## Common Pitfalls

1. **Wrong Pointer Order:** Moving pointers in incorrect order.
2. **Lost References:** Not storing next node before changing links.
3. **Complex Logic:** Overcomplicating the pointer manipulation.
4. **Wrong Return:** Returning wrong pointer as new head.
5. **Empty List:** Not handling empty list case properly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/206.reverse-linked-list.py)](../exercises/206.reverse-linked-list.py)

*Note: This is a classic linked list problem that demonstrates efficient iterative reversal with three pointers.*
