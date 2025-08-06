# Shortest Word Distance III

[![Problem 245](https://img.shields.io/badge/Problem-245-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/shortest-word-distance-iii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/shortest-word-distance-iii/)

**Problem Number:** [245](https://leetcode.com/problems/shortest-word-distance-iii/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/shortest-word-distance-iii/](https://leetcode.com/problems/shortest-word-distance-iii/)

## Problem Description

Given an array of strings `wordsDict` and two strings `word1` and `word2`, return *the shortest distance between these two words in the list*.

**Note** that `word1` and `word2` may be the same. It is guaranteed that they represent *two individual words* in the list.

**Example 1:**
```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
```

**Example 2:**
```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3
```

**Constraints:**
- `1 <= wordsDict.length <= 3 * 10^4`
- `1 <= wordsDict[i].length <= 10`
- `wordsDict[i]` consists of lowercase English letters.
- `word1` and `word2` are in `wordsDict`.

## My Approach

I used a **Hash Map with Two Pointers** approach that handles the case where word1 and word2 can be the same. The key insight is to use different strategies for same and different words.

**Algorithm:**
1. Create hash map to store word indices
2. Collect indices for word1 and word2
3. If word1 == word2:
   - Use nested loops to find minimum distance between different indices
4. If word1 != word2:
   - Use two-pointer approach to find minimum distance
5. Return minimum distance found

## Solution

The solution uses hash map and handles same word case with nested loops. See the implementation in the [solution file](../exercises/245.shortest-word-distance-iii.py).

**Key Points:**
- Uses hash map to store word indices
- Handles same word case with nested loops
- Uses two-pointer approach for different words
- Avoids comparing same indices when words are identical

## Time & Space Complexity

**Time Complexity:** O(n)
- Building hash map: O(n)
- Same word case: O(m²) where m is occurrences of the word
- Different words case: O(m + k) where m, k are occurrences
- Total: O(n)

**Space Complexity:** O(n)
- Hash map stores indices for all words
- Total: O(n)

## Key Insights

1. **Same Word Handling:** When word1 == word2, need to find distance between different indices.

2. **Nested Loops:** For same word, use nested loops to compare different indices.

3. **Two Pointers:** For different words, use two-pointer approach.

4. **Index Avoidance:** When words are same, avoid comparing same index with itself.

5. **Multiple Occurrences:** Handles cases where words appear multiple times.

6. **Efficient Lookup:** Hash map provides O(1) lookup for word indices.

## Mistakes Made

1. **Same Word Case:** Initially might not handle word1 == word2 case.

2. **Wrong Comparison:** Comparing same index with itself when words are identical.

3. **Complex Logic:** Overcomplicating the same word handling.

4. **Inefficient Approach:** Using same approach for both cases.

## Related Problems

- **Shortest Word Distance** (Problem 243): Different words only
- **Shortest Word Distance II** (Problem 244): Design class version
- **Two Sum** (Problem 1): Find pair with target sum
- **Container With Most Water** (Problem 11): Two-pointer approach

## Alternative Approaches

1. **Single Pass:** Track last seen indices during single pass - O(n) time, O(1) space
2. **Binary Search:** Use binary search on sorted indices - O(n log n) time
3. **Brute Force:** Check all pairs of indices - O(n²) time

## Common Pitfalls

1. **Same Word Case:** Not handling word1 == word2 case properly.
2. **Wrong Comparison:** Comparing same index with itself.
3. **Complex Logic:** Overcomplicating the same word handling.
4. **Inefficient Approach:** Using same approach for both cases.
5. **Memory Issues:** Not considering space complexity of storing indices.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/245.shortest-word-distance-iii.py)](../exercises/245.shortest-word-distance-iii.py)

*Note: This is a two-pointer problem that demonstrates handling same word case in distance calculation.*
