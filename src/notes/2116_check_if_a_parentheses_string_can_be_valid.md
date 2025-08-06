# Check if a Parentheses String Can Be Valid

[![Problem 2116](https://img.shields.io/badge/Problem-2116-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)

**Problem Number:** [2116](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** String, Greedy, Stack
**LeetCode Link:** [https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)

## Problem Description

A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is **valid** if **any** of the following conditions is **true**:

- It is `()`.
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.
- It can be written as `(A)`, where `A` is a valid parentheses string.

You are given a parentheses string `s` and a string `locked`, both of length `n`. `locked` is a binary string consisting only of `'0'`s and `'1'`s. For each index `i` of `s`:

- If `locked[i]` is `'1'`, you **cannot** change `s[i]`.
- But if `locked[i]` is `'0'`, you **can** change `s[i]` to either `'('` or `')'`.

Return `true` *if you can make* `s` *a valid parentheses string*. Otherwise, return `false`.

**Example 1:**
```
Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged.
Makes s valid: "((()))" .
```

**Example 2:**
```
Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
```

**Example 3:**
```
Input: s = ")", locked = "0"
Output: false
```

**Constraints:**
- `n == s.length == locked.length`
- `1 <= n <= 10^5`
- `s[i]` is either `'('` or `')'`.
- `locked[i]` is either `'0'` or `'1'`.

## My Approach

I used a **Greedy** approach with range tracking to check if the parentheses string can be made valid. The key insight is to track the minimum and maximum possible balance at each position.

**Algorithm:**
1. Check if string length is odd (impossible to make valid)
2. Initialize min and max balance to 0
3. For each character:
   - If locked and '(': increment both min and max
   - If locked and ')': decrement both min and max
   - If unlocked: decrement min, increment max
4. Ensure min balance never goes below 0
5. Return true if final balance can be 0

## Solution

The solution uses greedy approach with balance range tracking. See the implementation in the [solution file](../exercises/2116.check-if-a-parentheses-string-can-be-valid.py).

**Key Points:**
- Uses balance range tracking
- Handles locked and unlocked positions
- Ensures balance never goes negative
- Checks if final balance can be zero

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through string: O(n)
- Constant operations per character
- Total: O(n)

**Space Complexity:** O(1)
- Uses only constant extra space
- No additional data structures needed

## Key Insights

1. **Balance Range:** Track minimum and maximum possible balance.

2. **Locked Positions:** Must use exact character for locked positions.

3. **Unlocked Positions:** Can choose '(' or ')' to adjust balance.

4. **Negative Balance:** Never allow balance to go below 0.

5. **Final Balance:** Must end with balance of 0 for valid string.

6. **Odd Length:** Impossible to make valid if length is odd.

## Mistakes Made

1. **Wrong Balance:** Initially might not track balance range correctly.

2. **Complex Logic:** Overcomplicating the balance calculation.

3. **Edge Cases:** Not handling odd length strings.

4. **Inefficient Approach:** Using stack approach when greedy suffices.

## Related Problems

- **Valid Parentheses** (Problem 20): Check if parentheses are valid
- **Generate Parentheses** (Problem 22): Generate valid parentheses
- **Longest Valid Parentheses** (Problem 32): Find longest valid substring
- **Remove Invalid Parentheses** (Problem 301): Remove invalid parentheses

## Alternative Approaches

1. **Stack:** Use stack to track parentheses - O(n) time, O(n) space
2. **Two Pass:** Check from left and right - O(n) time, O(1) space
3. **Dynamic Programming:** Use DP for complex cases - O(n²) time

## Common Pitfalls

1. **Wrong Balance:** Not tracking balance range correctly.
2. **Complex Logic:** Overcomplicating the balance calculation.
3. **Edge Cases:** Not handling odd length strings.
4. **Inefficient Approach:** Using stack approach when greedy suffices.
5. **Locked Positions:** Not properly handling locked vs unlocked positions.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/2116.check-if-a-parentheses-string-can-be-valid.py)](../exercises/2116.check-if-a-parentheses-string-can-be-valid.py)

*Note: This is a greedy problem that demonstrates balance range tracking for parentheses validation.*
