# Shortest Word Distance

[![Problem 243](https://img.shields.io/badge/Problem-243-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/shortest-word-distance/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/shortest-word-distance/)

**Problem Number:** [243](https://leetcode.com/problems/shortest-word-distance/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/shortest-word-distance/](https://leetcode.com/problems/shortest-word-distance/)

## Problem Description

Given an array of strings `wordsDict` and two different strings `word1` and `word2`, return *the shortest distance between these two words in the list*.

**Example 1:**
```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
```

**Example 2:**
```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
```

**Constraints:**
- `1 <= wordsDict.length <= 3 * 10^4`
- `1 <= wordsDict[i].length <= 10`
- `word1` and `word2` are in `wordsDict`.
- `word1 != word2`

## My Approach

I used a **Hash Map with Two Pointers** approach to find the shortest distance. The key insight is to collect all indices of both words and then use two pointers to find the minimum distance.

**Algorithm:**
1. Create hash map to store word indices
2. Collect all indices for word1 and word2
3. Use two pointers to traverse both index lists
4. Calculate distance between current indices
5. Move pointer with smaller index to find minimum distance
6. Return minimum distance found

## Solution

The solution uses hash map and two pointers to efficiently find shortest distance. See the implementation in the [solution file](../exercises/243.shortest-word-distance.py).

**Key Points:**
- Uses hash map to store word indices
- Two-pointer approach for efficient traversal
- Calculates minimum distance between all pairs
- Handles multiple occurrences of words

## Time & Space Complexity

**Time Complexity:** O(n)
- Building hash map: O(n)
- Two-pointer traversal: O(m + k) where m, k are occurrences of word1, word2
- Total: O(n)

**Space Complexity:** O(n)
- Hash map stores indices for all words
- In worst case: O(n)

## Key Insights

1. **Index Collection:** Collecting all indices allows efficient distance calculation.

2. **Two Pointers:** Using two pointers on sorted indices is optimal.

3. **Sorted Indices:** Indices are naturally sorted in order of appearance.

4. **Minimum Distance:** Always move the pointer with smaller index.

5. **Multiple Occurrences:** Handles cases where words appear multiple times.

6. **Efficient Traversal:** Two-pointer approach avoids checking all pairs.

## Mistakes Made

1. **Brute Force:** Initially might check all pairs of indices.

2. **Wrong Order:** Not understanding the two-pointer traversal order.

3. **Complex Logic:** Overcomplicating the distance calculation.

4. **Inefficient Approach:** Using nested loops instead of two pointers.

## Related Problems

- **Shortest Word Distance II** (Problem 244): Design class for multiple queries
- **Shortest Word Distance III** (Problem 245): Handle case where word1 == word2
- **Two Sum** (Problem 1): Find pair with target sum
- **Container With Most Water** (Problem 11): Two-pointer approach

## Alternative Approaches

1. **Single Pass:** Track last seen indices during single pass - O(n) time, O(1) space
2. **Binary Search:** Use binary search on sorted indices - O(n log n) time
3. **Brute Force:** Check all pairs of indices - O(n²) time

## Common Pitfalls

1. **Brute Force:** Using nested loops to check all pairs.
2. **Wrong Order:** Not understanding the two-pointer traversal order.
3. **Complex Logic:** Overcomplicating the distance calculation.
4. **Inefficient Approach:** Using O(n²) approach when O(n) is possible.
5. **Memory Issues:** Not considering space complexity of storing indices.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/243.shortest-word-distance.py)](../exercises/243.shortest-word-distance.py)

*Note: This is a two-pointer problem that demonstrates efficient distance calculation between word indices.*
