# Plus One

[![Problem 66](https://img.shields.io/badge/Problem-66-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/plus-one/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/plus-one/)

**Problem Number:** [66](https://leetcode.com/problems/plus-one/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Math
**LeetCode Link:** [https://leetcode.com/problems/plus-one/](https://leetcode.com/problems/plus-one/)

## Problem Description

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i^th` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

**Example 2:**
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

**Example 3:**
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

**Constraints:**
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`'s

## My Approach

I used a **Recursive** approach to handle the carry-over logic. The key insight is to process digits from right to left, handling carry-over when a digit becomes 10, and adding a new digit at the beginning if needed.

**Algorithm:**
1. Use a recursive helper function to process digits from right to left
2. For each digit, add the carry-over (or 1 for the first call)
3. If the sum is less than 10, update the digit and return
4. If the sum is 10 or more, set the digit to the remainder and carry over the quotient
5. If we reach the beginning and still have carry-over, insert a new digit at the beginning

## Solution

The solution uses recursion to handle carry-over logic. See the implementation in the [solution file](../exercises/66.plus-one.py).

**Key Points:**
- Uses recursion to process digits from right to left
- Handles carry-over when digit sum exceeds 9
- Inserts new digit at beginning when needed
- Processes carry-over recursively until resolved
- Maintains the original array structure

## Time & Space Complexity

**Time Complexity:** O(n)
- In worst case, we process all digits once
- Each recursive call processes one digit
- Total: O(n)

**Space Complexity:** O(n)
- Recursion stack depth: O(n) in worst case
- Each recursive call uses constant space
- Total: O(n)

## Key Insights

1. **Right-to-Left Processing:** We process digits from least significant to most significant to handle carry-over correctly.

2. **Carry-Over Logic:** When a digit becomes 10, we carry over 1 to the next digit and set current digit to 0.

3. **Recursive Approach:** Using recursion makes the carry-over logic clean and easy to understand.

4. **Array Insertion:** When we need to add a new digit (like 9 + 1 = 10), we insert it at the beginning.

5. **Base Case:** The recursion stops when we either process all digits or have no carry-over.

6. **Digit Constraints:** Each digit must be between 0 and 9, and we handle overflow by carrying over.

## Mistakes Made

1. **Left-to-Right Processing:** Initially might process from left to right, which complicates carry-over handling.

2. **Complex Logic:** Overcomplicating the solution with unnecessary loops or conditions.

3. **Wrong Carry Handling:** Not properly handling carry-over when digits sum to 10 or more.

4. **Array Manipulation:** Not efficiently handling the case where we need to add a new digit.

## Related Problems

- **Add Two Numbers** (Problem 2): Add two numbers represented as linked lists
- **Multiply Strings** (Problem 43): Multiply two numbers represented as strings
- **Add Binary** (Problem 67): Add two binary strings
- **Add Strings** (Problem 415): Add two numbers represented as strings

## Alternative Approaches

1. **Iterative:** Use a loop to process digits from right to left - O(n) time, O(1) space
2. **String Conversion:** Convert to integer, add one, convert back - O(n) time, O(n) space
3. **In-Place Modification:** Modify the array in-place without recursion

## Common Pitfalls

1. **Wrong Direction:** Processing digits from left to right instead of right to left.
2. **Complex Logic:** Overcomplicating the carry-over handling.
3. **Array Manipulation:** Not efficiently handling the case where array length increases.
4. **Recursion Depth:** Not considering stack overflow for very large arrays.
5. **Carry Handling:** Not properly handling carry-over when digits sum to 10.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/66.plus-one.py)](../exercises/66.plus-one.py)

*Note: This is a fundamental array manipulation problem that demonstrates efficient handling of carry-over in digit arithmetic.*
