# Longest Palindromic Substring

[![Problem 5](https://img.shields.io/badge/Problem-5-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-palindromic-substring/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-palindromic-substring/)

**Problem Number:** [5](https://leetcode.com/problems/longest-palindromic-substring/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** String, Dynamic Programming
**LeetCode Link:** [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem Description

Given a string `s`, return the longest palindromic substring in `s`.

**Example 1:**
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

**Constraints:**
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters

## My Approach

I used the **Expand Around Center** approach, which is one of the most efficient methods for finding palindromes. The key insight is to consider each character (and each pair of adjacent characters) as a potential center of a palindrome and expand outward.

**Algorithm:**
1. Handle edge cases (empty string or single character)
2. For each character in the string, treat it as a center and expand
3. For each pair of adjacent characters, treat them as a center and expand
4. Keep track of the longest palindrome found
5. Return the longest palindromic substring

## Solution

The solution uses the expand around center technique. See the implementation in the [solution file](../exercises/5.longest-palindromic-substring.py).

**Key Points:**
- Uses a helper function to expand from a given center
- Handles both odd-length (single character center) and even-length (two character center) palindromes
- Tracks the maximum length and corresponding substring
- Efficiently explores all possible palindrome centers

## Time & Space Complexity

**Time Complexity:** O(n²)
- We iterate through each character as a potential center: O(n)
- For each center, we expand outward: O(n) in worst case
- Total: O(n²)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures proportional to input size

## Key Insights

1. **Expand Around Center:** Instead of checking all possible substrings, we expand from potential centers.

2. **Two Types of Centers:** We need to consider both single characters (odd-length palindromes) and adjacent character pairs (even-length palindromes).

3. **Symmetric Expansion:** When expanding from a center, we move left and right simultaneously, checking if characters match.

4. **Early Termination:** The expansion stops as soon as we encounter non-matching characters.

5. **Length Calculation:** The length of a palindrome is (right - left + 1) after expansion.

6. **Edge Case Handling:** Single characters and empty strings are always palindromes.

## Mistakes Made

1. **Missing Even-Length Palindromes:** Initially might only consider single character centers, missing palindromes like "aa".

2. **Boundary Conditions:** Not properly handling cases where expansion reaches string boundaries.

3. **Length Tracking:** Incorrectly calculating or updating the maximum length.

4. **String Slicing:** Inefficient string slicing operations in the expansion process.

## Related Problems

- **Palindromic Substrings** (Problem 647): Count all palindromic substrings
- **Valid Palindrome** (Problem 125): Check if a string is a palindrome
- **Palindrome Partitioning** (Problem 131): Partition string into palindromic substrings
- **Longest Palindromic Subsequence** (Problem 516): Find longest palindromic subsequence

## Alternative Approaches

1. **Dynamic Programming:** Use a 2D DP table - O(n²) time, O(n²) space
2. **Manacher's Algorithm:** More complex but achieves O(n) time complexity
3. **Brute Force:** Check all possible substrings - O(n³) time complexity

## Common Pitfalls

1. **Only Odd-Length Palindromes:** Forgetting to check even-length palindromes.
2. **Inefficient Expansion:** Not optimizing the expansion process.
3. **Boundary Issues:** Not handling cases where expansion reaches string ends.
4. **String Operations:** Using expensive string operations during expansion.
5. **Memory Usage:** Creating unnecessary copies of substrings.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/5.longest-palindromic-substring.py)](../exercises/5.longest-palindromic-substring.py)

*Note: This is a classic string problem that introduces the expand around center technique, widely used in palindrome-related problems.*
