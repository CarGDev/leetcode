# Reverse Words in a String

[![Problem 151](https://img.shields.io/badge/Problem-151-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/reverse-words-in-a-string/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/reverse-words-in-a-string/)

**Problem Number:** [151](https://leetcode.com/problems/reverse-words-in-a-string/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** String, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/reverse-words-in-a-string/](https://leetcode.com/problems/reverse-words-in-a-string/)

## Problem Description

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Example 1:**
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**
```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**Example 3:**
```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

## My Approach

I used a **String Manipulation** approach with array reversal. The key insight is to split the string into words, reverse their order, and then join them back together.

**Algorithm:**
1. Split the input string by spaces to get individual words
2. Create a new array to store words in reverse order
3. Iterate through the original words array
4. Skip empty strings (multiple spaces)
5. Place non-empty words in reverse positions in the new array
6. Join the reversed words with single spaces
7. Remove any leading/trailing spaces

## Solution

The solution uses string manipulation with array reversal. See the implementation in the [solution file](../exercises/151.reverse-words-in-a-string.py).

**Key Points:**
- Splits string by spaces to get individual words
- Skips empty strings from multiple spaces
- Reverses word order using array manipulation
- Joins words with single spaces
- Removes leading/trailing spaces

## Time & Space Complexity

**Time Complexity:** O(n)
- String split: O(n)
- Array iteration: O(n)
- String join: O(n)
- Total: O(n)

**Space Complexity:** O(n)
- Split array: O(n)
- Reversed array: O(n)
- Total: O(n)

## Key Insights

1. **String Split:** Using split() method handles multiple spaces automatically.

2. **Empty String Filtering:** Skipping empty strings handles multiple consecutive spaces.

3. **Array Reversal:** Using array manipulation is more efficient than string operations.

4. **Space Handling:** The split and join operations naturally handle space normalization.

5. **Edge Cases:** The approach handles leading/trailing spaces and multiple spaces between words.

6. **Efficient Joining:** Using join() is more efficient than string concatenation.

## Mistakes Made

1. **Manual Space Handling:** Initially might manually handle spaces instead of using split().

2. **String Concatenation:** Using string concatenation instead of array join.

3. **Complex Logic:** Overcomplicating the word reversal process.

4. **Space Issues:** Not properly handling multiple spaces between words.

## Related Problems

- **Reverse Words in a String III** (Problem 557): Reverse individual words
- **Valid Palindrome** (Problem 125): Check if string is palindrome
- **Longest Common Prefix** (Problem 14): Find common prefix
- **Valid Parentheses** (Problem 20): Check valid parentheses

## Alternative Approaches

1. **Two Pointers:** Use two pointers to reverse words in-place - O(n) time, O(1) space
2. **Stack-based:** Use stack to reverse word order - O(n) time, O(n) space
3. **Recursive:** Use recursion to reverse words - O(n) time, O(n) space

## Common Pitfalls

1. **Manual Space Handling:** Manually handling spaces instead of using built-in methods.
2. **String Concatenation:** Using inefficient string concatenation.
3. **Complex Logic:** Overcomplicating the word reversal process.
4. **Space Issues:** Not properly handling multiple spaces between words.
5. **Edge Cases:** Not handling leading/trailing spaces properly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/151.reverse-words-in-a-string.py)](../exercises/151.reverse-words-in-a-string.py)

*Note: This is a string manipulation problem that demonstrates efficient word reversal with array operations.*
