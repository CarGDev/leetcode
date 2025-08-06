# Happy Number

[![Problem 202](https://img.shields.io/badge/Problem-202-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/happy-number/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/happy-number/)

**Problem Number:** [202](https://leetcode.com/problems/happy-number/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, Math, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/happy-number/](https://leetcode.com/problems/happy-number/)

## Problem Description

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return `true` if `n` is a happy number, and `false` if not.

**Example 1:**
```
Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
```

**Example 2:**
```
Input: n = 2
Output: false
```

**Constraints:**
- `1 <= n <= 2^31 - 1`

## My Approach

I used a **Hash Set** approach with recursion to detect cycles. The key insight is to track visited numbers to detect infinite loops and use recursion to process the happy number sequence.

**Algorithm:**
1. Use a memo list to track visited numbers
2. If current number is already visited, return False (cycle detected)
3. Add current number to memo
4. Calculate sum of squares of digits
5. If sum equals 1, return True
6. Otherwise, recursively call with the new sum

## Solution

The solution uses hash set and recursion to detect cycles in the happy number sequence. See the implementation in the [solution file](../exercises/202.happy-number.py).

**Key Points:**
- Uses memo list to track visited numbers
- Detects cycles to avoid infinite loops
- Recursively processes digit squares
- Returns True when sum equals 1
- Returns False when cycle is detected

## Time & Space Complexity

**Time Complexity:** O(log n)
- Each iteration reduces the number significantly
- Cycle detection limits the number of iterations
- Total: O(log n)

**Space Complexity:** O(log n)
- Memo list stores visited numbers
- Number of visited numbers is bounded by O(log n)
- Total: O(log n)

## Key Insights

1. **Cycle Detection:** Using a hash set to detect cycles prevents infinite loops.

2. **Digit Extraction:** Using modulo and division to extract digits efficiently.

3. **Recursive Process:** The happy number process naturally fits recursion.

4. **Termination:** The process either reaches 1 or enters a cycle.

5. **Mathematical Property:** Happy numbers have a mathematical pattern.

6. **Bounded Space:** The number of visited values is bounded.

## Mistakes Made

1. **No Cycle Detection:** Initially might not detect cycles, leading to infinite loops.

2. **Wrong Termination:** Not properly handling the termination condition.

3. **Complex Logic:** Overcomplicating the digit extraction process.

4. **Space Issues:** Not considering the space complexity of tracking visited numbers.

## Related Problems

- **Linked List Cycle** (Problem 141): Detect cycle in linked list
- **Linked List Cycle II** (Problem 142): Find cycle start point
- **Find the Duplicate Number** (Problem 287): Find duplicate using cycle detection
- **Add Digits** (Problem 258): Add digits until single digit

## Alternative Approaches

1. **Two Pointers (Floyd's):** Use fast and slow pointers - O(log n) time, O(1) space
2. **Iterative:** Use while loop instead of recursion - O(log n) time, O(log n) space
3. **Mathematical:** Use mathematical properties to optimize - O(log n) time

## Common Pitfalls

1. **No Cycle Detection:** Not detecting cycles leading to infinite loops.
2. **Wrong Termination:** Not properly handling when sum equals 1.
3. **Complex Logic:** Overcomplicating the digit extraction.
4. **Space Issues:** Not considering space complexity of tracking visited numbers.
5. **Recursion Depth:** Not considering recursion stack space.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/202.happy-number.py)](../exercises/202.happy-number.py)

*Note: This is a cycle detection problem that demonstrates efficient happy number checking with hash set.*
