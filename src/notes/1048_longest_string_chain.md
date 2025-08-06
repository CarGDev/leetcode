# Longest String Chain

[![Problem 1048](https://img.shields.io/badge/Problem-1048-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-string-chain/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-string-chain/)

**Problem Number:** [1048](https://leetcode.com/problems/longest-string-chain/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Hash Table, String, Dynamic Programming
**LeetCode Link:** [https://leetcode.com/problems/longest-string-chain/](https://leetcode.com/problems/longest-string-chain/)

## Problem Description

You are given an array of `words` where each word consists of lowercase English letters.

`wordA` is a predecessor of `wordB` if and only if we can insert exactly one letter anywhere in `wordA` without changing the order of the other characters to make it equal to `wordB`.

- For example, `"abc"` is a predecessor of `"abac"`, while `"cba"` is not a predecessor of `"bcad"`.

A word chain is a sequence of words `[word1, word2, ..., wordk]` with `k >= 1`, where `word1` is a predecessor of `word2`, `word2` is a predecessor of `word3`, and so on. A single word is trivially a word chain with `k == 1`.

Return the length of the longest possible word chain with words chosen from the given list of `words`.

**Example 1:**
```
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
```

**Example 2:**
```
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be used in the word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
```

**Example 3:**
```
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because "abcd" is not a predecessor of "dbqca".
```

**Constraints:**
- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 16`
- `words[i]` consists of lowercase English letters

## My Approach

I used a **Dynamic Programming** approach with hash table caching. The key insight is to sort words by length first, then for each word, try removing one character at a time to find its predecessors and build the longest chain.

**Algorithm:**
1. Sort words by length to process shorter words first
2. Use a hash table (cache) to store the longest chain ending at each word
3. For each word, try removing one character at each position
4. Check if the resulting substring exists in cache
5. Update the current word's chain length as max of all predecessors + 1
6. Track the maximum chain length found

## Solution

The solution uses dynamic programming with hash table caching. See the implementation in the [solution file](../exercises/1048.longest-string-chain.js).

**Key Points:**
- Sorts words by length to process in correct order
- Uses hash table to cache longest chain for each word
- Tries removing one character at each position to find predecessors
- Updates chain length based on predecessor lengths
- Tracks maximum chain length throughout the process

## Time & Space Complexity

**Time Complexity:** O(n × L²)
- n is the number of words
- L is the maximum word length
- Sorting: O(n log n)
- For each word, we try L positions and string slicing takes O(L)
- Total: O(n × L²)

**Space Complexity:** O(n)
- Hash table stores at most n words
- Each word can be up to length L
- Total: O(n × L)

## Key Insights

1. **Sorting by Length:** Processing words in order of increasing length ensures we build chains correctly.

2. **Predecessor Relationship:** A word is a predecessor if removing one character makes it equal to another word.

3. **Dynamic Programming:** Using a cache to store the longest chain ending at each word avoids recalculation.

4. **Character Removal:** For each word, we try removing one character at each position to find all possible predecessors.

5. **Chain Building:** The chain length for a word is the maximum of all its predecessors' chain lengths plus 1.

6. **Efficient Lookup:** Using a hash table provides O(1) lookup time for checking predecessors.

## Mistakes Made

1. **Wrong Order:** Not sorting words by length, leading to incorrect chain building.

2. **Inefficient Predecessor Check:** Using complex string matching instead of simple character removal.

3. **Missing Caching:** Not using memoization, leading to redundant calculations.

4. **Wrong Chain Logic:** Not properly updating chain lengths based on predecessors.

## Related Problems

- **Longest Increasing Subsequence** (Problem 300): Find longest increasing subsequence
- **Word Break** (Problem 139): Check if string can be segmented
- **Longest Common Subsequence** (Problem 1143): Find longest common subsequence
- **Edit Distance** (Problem 72): Calculate minimum edit distance

## Alternative Approaches

1. **Graph-based:** Build a graph where edges represent predecessor relationships - O(n² × L) time
2. **Topological Sort:** Use topological sort on the predecessor graph
3. **BFS:** Use breadth-first search to find longest path in the graph

## Common Pitfalls

1. **Wrong Processing Order:** Not sorting words by length.
2. **Inefficient Predecessor Finding:** Using complex string algorithms instead of simple character removal.
3. **Missing Caching:** Not using memoization to avoid redundant calculations.
4. **Wrong Chain Logic:** Not properly building chains based on predecessor relationships.
5. **String Operations:** Not considering the cost of string slicing operations.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/1048.longest-string-chain.js)](../exercises/1048.longest-string-chain.js)

*Note: This is a dynamic programming problem that demonstrates efficient string chain building with predecessor relationships.*
