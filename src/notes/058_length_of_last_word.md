# Length of Last Word

[![Problem 58](https://img.shields.io/badge/Problem-58-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/length-of-last-word/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/length-of-last-word/)

**Problem Number:** [58](https://leetcode.com/problems/length-of-last-word/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** String
**LeetCode Link:** [https://leetcode.com/problems/length-of-last-word/](https://leetcode.com/problems/length-of-last-word/)

## Problem Description

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

**Example 1:**
```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**
```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**
```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`
- There will be at least one word in `s`

## My Approach

I used a **String Manipulation** approach with built-in functions. The key insight is to strip leading and trailing spaces, then split the string by spaces to get the last word.

**Algorithm:**
1. Strip leading and trailing whitespace from the string
2. Split the string by spaces to get an array of words
3. Return the length of the last word in the array

## Solution

The solution uses string manipulation with built-in functions. See the implementation in the [solution file](../exercises/58.length-of-last-word.py).

**Key Points:**
- Uses strip() to remove leading and trailing spaces
- Uses split() to separate words by spaces
- Returns length of the last word in the resulting array
- Handles multiple spaces between words automatically
- Simple and efficient approach

## Time & Space Complexity

**Time Complexity:** O(n)
- strip() operation: O(n)
- split() operation: O(n)
- length calculation: O(1)
- Total: O(n)

**Space Complexity:** O(n)
- split() creates a new array of words
- Each word can be up to length n
- Total: O(n)

## Key Insights

1. **String Manipulation:** Using built-in string functions makes the solution simple and readable.

2. **Whitespace Handling:** strip() automatically handles leading and trailing spaces.

3. **Word Separation:** split() with default delimiter (space) handles multiple spaces between words.

4. **Last Word Access:** Using negative indexing (-1) provides easy access to the last element.

5. **Edge Case Handling:** The approach naturally handles strings with multiple spaces.

6. **Built-in Efficiency:** Python's built-in string functions are optimized for performance.

## Mistakes Made

1. **Manual Parsing:** Initially might try to manually parse the string character by character.

2. **Wrong Split:** Not using split() or using wrong delimiter.

3. **Missing Strip:** Not removing leading/trailing spaces before processing.

4. **Complex Logic:** Overcomplicating the solution with unnecessary loops.

## Related Problems

- **Reverse Words in a String** (Problem 151): Reverse the order of words in a string
- **Valid Palindrome** (Problem 125): Check if a string is a palindrome
- **Longest Common Prefix** (Problem 14): Find common prefix among strings
- **Valid Parentheses** (Problem 20): Check if parentheses are valid

## Alternative Approaches

1. **Manual Parsing:** Iterate from end to find last word - O(n) time, O(1) space
2. **Regular Expressions:** Use regex to find last word - O(n) time complexity
3. **Two Pointers:** Use pointers to find word boundaries - O(n) time, O(1) space

## Common Pitfalls

1. **Manual Parsing:** Using complex loops instead of built-in functions.
2. **Wrong Split:** Not using split() or using incorrect delimiter.
3. **Missing Strip:** Not handling leading/trailing spaces.
4. **Index Errors:** Not properly accessing the last element.
5. **Over-engineering:** Using unnecessary data structures or complex logic.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/58.length-of-last-word.py)](../exercises/58.length-of-last-word.py)

*Note: This is a simple string manipulation problem that demonstrates efficient use of built-in string functions.*
