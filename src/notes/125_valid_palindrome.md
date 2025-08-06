# Valid Palindrome

[![Problem 125](https://img.shields.io/badge/Problem-125-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/valid-palindrome/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/valid-palindrome/)

**Problem Number:** [125](https://leetcode.com/problems/valid-palindrome/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** String, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)

## Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints:**
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters

## My Approach

I used a **String Manipulation** approach with regular expressions. The key insight is to clean the string by removing non-alphanumeric characters and converting to lowercase, then check if it reads the same forward and backward.

**Algorithm:**
1. Use regular expression to remove all non-alphanumeric characters
2. Convert the cleaned string to lowercase
3. Create a reversed version of the string
4. Compare the original cleaned string with its reverse
5. Return true if they are equal, false otherwise

## Solution

The solution uses string manipulation with regular expressions. See the implementation in the [solution file](../exercises/125.valid-palindrome.py).

**Key Points:**
- Uses regex to remove non-alphanumeric characters
- Converts to lowercase for case-insensitive comparison
- Creates reversed string for comparison
- Simple and efficient approach
- Handles edge cases like empty strings

## Time & Space Complexity

**Time Complexity:** O(n)
- Regex substitution: O(n)
- String reversal: O(n)
- String comparison: O(n)
- Total: O(n)

**Space Complexity:** O(n)
- Creates new strings for cleaned and reversed versions
- Each string can be up to length n
- Total: O(n)

## Key Insights

1. **String Cleaning:** Using regex to remove non-alphanumeric characters is efficient and clean.

2. **Case Insensitivity:** Converting to lowercase ensures case-insensitive comparison.

3. **Palindrome Check:** Comparing a string with its reverse is a simple way to check for palindromes.

4. **Character Filtering:** Only alphanumeric characters matter for palindrome validation.

5. **Edge Cases:** Empty strings and strings with only non-alphanumeric characters are valid palindromes.

6. **Built-in Functions:** Using Python's built-in string operations makes the solution concise.

## Mistakes Made

1. **Manual Filtering:** Initially might manually iterate through characters instead of using regex.

2. **Case Sensitivity:** Not converting to lowercase for case-insensitive comparison.

3. **Complex Logic:** Overcomplicating the palindrome check with two pointers.

4. **Wrong Characters:** Not properly filtering non-alphanumeric characters.

## Related Problems

- **Valid Palindrome II** (Problem 680): Check if string can be palindrome after removing one character
- **Longest Palindromic Substring** (Problem 5): Find longest palindromic substring
- **Palindrome Number** (Problem 9): Check if number is palindrome
- **Palindrome Linked List** (Problem 234): Check if linked list is palindrome

## Alternative Approaches

1. **Two Pointers:** Use left and right pointers to compare characters - O(n) time, O(1) space
2. **Stack-based:** Use stack to reverse and compare - O(n) time, O(n) space
3. **Recursive:** Use recursion to check palindrome - O(n) time, O(n) space

## Common Pitfalls

1. **Manual Filtering:** Manually iterating through characters instead of using regex.
2. **Case Sensitivity:** Not handling case-insensitive comparison.
3. **Complex Implementation:** Using two pointers when simple string comparison suffices.
4. **Wrong Characters:** Not properly filtering non-alphanumeric characters.
5. **Edge Cases:** Not handling empty strings or strings with only special characters.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/125.valid-palindrome.py)](../exercises/125.valid-palindrome.py)

*Note: This is a simple string manipulation problem that demonstrates efficient palindrome checking with regex.*
