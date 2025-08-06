# Valid Parentheses

[![Problem 20](https://img.shields.io/badge/Problem-20-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/valid-parentheses/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/valid-parentheses/)

**Problem Number:** [20](https://leetcode.com/problems/valid-parentheses/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** String, Stack
**LeetCode Link:** [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`

## My Approach

I used a **Stack** approach to validate the parentheses. The key insight is to use a stack to keep track of opening brackets and match them with closing brackets in the correct order.

**Algorithm:**
1. Create a hash map mapping closing brackets to their corresponding opening brackets
2. Initialize an empty stack
3. Iterate through each character in the string
4. If it's an opening bracket, push it onto the stack
5. If it's a closing bracket, check if the top of stack matches the corresponding opening bracket
6. If match found, pop from stack; otherwise return false
7. Return true if stack is empty at the end

## Solution

The solution uses a stack to validate parentheses matching. See the implementation in the [solution file](../exercises/20.valid-parentheses.py).

**Key Points:**
- Uses a hash map to map closing brackets to opening brackets
- Stack stores opening brackets in order of appearance
- Validates matching brackets and correct order
- Handles edge cases like empty string and single characters

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the string once
- Stack operations (push/pop) are O(1)
- Hash map lookups are O(1)
- Total: O(n)

**Space Complexity:** O(n)
- Stack can store up to n/2 opening brackets in worst case
- Hash map has constant size (3 pairs)
- Total: O(n)

## Key Insights

1. **Stack for Order Tracking:** Stack naturally handles the "last in, first out" order required for parentheses matching.

2. **Hash Map for Mapping:** Using a hash map to map closing brackets to opening brackets makes the code cleaner and more efficient.

3. **Early Termination:** We can return false immediately when we encounter a mismatch or when trying to pop from an empty stack.

4. **Stack Empty Check:** At the end, the stack must be empty for the string to be valid (all brackets must be matched).

5. **Single Character Handling:** Strings with odd length or single characters are automatically invalid.

6. **Order Validation:** The stack ensures that brackets are closed in the correct order (most recent opening bracket must be closed first).

## Mistakes Made

1. **Wrong Data Structure:** Initially might use a simple counter approach, which doesn't handle order correctly.

2. **Missing Edge Cases:** Not properly handling empty strings or strings with single characters.

3. **Incorrect Mapping:** Using wrong mapping between opening and closing brackets.

4. **Stack Empty Check:** Forgetting to check if the stack is empty at the end.

## Related Problems

- **Generate Parentheses** (Problem 22): Generate all valid parentheses combinations
- **Longest Valid Parentheses** (Problem 32): Find longest valid parentheses substring
- **Remove Invalid Parentheses** (Problem 301): Remove minimum parentheses to make string valid
- **Check If a Parentheses String Can Be Valid** (Problem 2116): More complex validation

## Alternative Approaches

1. **Counter Approach:** Use counters for each bracket type (doesn't handle order correctly)
2. **Recursive:** Use recursion to validate nested parentheses
3. **Two Pass:** First pass to count brackets, second pass to validate order

## Common Pitfalls

1. **Wrong Order Handling:** Not using a stack and thus not handling the order correctly.
2. **Missing Edge Cases:** Not handling empty strings or single characters.
3. **Incorrect Mapping:** Using wrong bracket pairs in the mapping.
4. **Stack Empty Check:** Not checking if the stack is empty at the end.
5. **Early Termination:** Not returning false immediately when encountering mismatches.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/20.valid-parentheses.py)](../exercises/20.valid-parentheses.py)

*Note: This is a fundamental stack problem that introduces the concept of using a stack to validate matching pairs in the correct order.*
