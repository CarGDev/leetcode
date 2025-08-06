# Maximum Difference Between Even and Odd Frequency I

[![Problem 3442](https://img.shields.io/badge/Problem-3442-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)

**Problem Number:** [3442](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, String, Counting
**LeetCode Link:** [https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)

## Problem Description

Given a string `s`, return *the **maximum difference** between the frequency of any two characters that have different frequencies*.

The frequency of a character is the number of times it appears in the string.

**Example 1:**
```
Input: s = "aab"
Output: 0
Explanation: The frequency of 'a' is 2, and the frequency of 'b' is 1.
The maximum difference between frequencies is 2 - 1 = 1.
```

**Example 2:**
```
Input: s = "abcabc"
Output: 3
Explanation: The frequency of 'a' is 2, the frequency of 'b' is 2, and the frequency of 'c' is 2.
The maximum difference between frequencies is 2 - 2 = 0.
```

**Constraints:**
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## My Approach

I used a **Hash Table** approach to count character frequencies and find the maximum difference. The key insight is to track the maximum odd frequency and minimum even frequency separately.

**Algorithm:**
1. Use Counter to count character frequencies
2. Initialize max_odd to 0 and min_even to infinity
3. Iterate through frequency values:
   - If frequency is even, update min_even
   - If frequency is odd, update max_odd
4. Return max_odd - min_even

## Solution

The solution uses hash table to count frequencies and find maximum difference. See the implementation in the [solution file](../exercises/3442.maximum-difference-between-even-and-odd-frequency-i.py).

**Key Points:**
- Uses Counter for frequency counting
- Tracks maximum odd and minimum even frequencies
- Handles edge cases properly
- Simple and efficient approach

## Time & Space Complexity

**Time Complexity:** O(n)
- Counter creation: O(n)
- Single pass through frequency values: O(k) where k is unique characters
- Total: O(n)

**Space Complexity:** O(k)
- Counter stores frequency of each unique character
- k is the number of unique characters
- In worst case: O(n)

## Key Insights

1. **Frequency Counting:** Using Counter provides efficient frequency counting.

2. **Even/Odd Separation:** Track even and odd frequencies separately.

3. **Maximum Difference:** Find max odd frequency - min even frequency.

4. **Edge Cases:** Handle cases where no even or odd frequencies exist.

5. **Character Set:** Works with any lowercase English letters.

6. **Simple Logic:** The solution logic is straightforward and efficient.

## Mistakes Made

1. **Wrong Logic:** Initially might not separate even and odd frequencies.

2. **Complex Approach:** Overcomplicating the frequency difference calculation.

3. **Edge Cases:** Not handling cases where no even or odd frequencies exist.

4. **Wrong Data Structure:** Not using appropriate data structure for counting.

## Related Problems

- **Maximum Difference Between Even and Odd Frequency II** (Problem 3445): Similar problem with different constraints
- **Valid Anagram** (Problem 242): Character frequency comparison
- **Group Anagrams** (Problem 49): Group strings by character frequency
- **First Unique Character** (Problem 387): Find first unique character

## Alternative Approaches

1. **Manual Counting:** Use manual hash map for counting - O(n) time, O(n) space
2. **Array Counting:** Use array for ASCII characters - O(n) time, O(1) space
3. **Sorting:** Sort frequencies and find difference - O(n log n) time, O(n) space

## Common Pitfalls

1. **Wrong Logic:** Not separating even and odd frequencies properly.
2. **Complex Approach:** Overcomplicating the frequency difference calculation.
3. **Edge Cases:** Not handling cases where no even or odd frequencies exist.
4. **Wrong Data Structure:** Not using appropriate data structure for counting.
5. **Inefficient Approach:** Using O(n²) approach when O(n) suffices.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/3442.maximum-difference-between-even-and-odd-frequency-i.py)](../exercises/3442.maximum-difference-between-even-and-odd-frequency-i.py)

*Note: This is a hash table problem that demonstrates efficient frequency counting and difference calculation.*
