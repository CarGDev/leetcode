# Shortest Word Distance II

[![Problem 244](https://img.shields.io/badge/Problem-244-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/shortest-word-distance-ii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/shortest-word-distance-ii/)

**Problem Number:** [244](https://leetcode.com/problems/shortest-word-distance-ii/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Hash Table, Design, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/shortest-word-distance-ii/](https://leetcode.com/problems/shortest-word-distance-ii/)

## Problem Description

Design a data structure that will be initialized with a string array, and then it will answer queries of the shortest distance between two different strings from the array.

Implement the `WordDistance` class:

- `WordDistance(String[] wordsDict)` initializes the object with the strings array `wordsDict`.
- `int shortest(String word1, String word2)` returns the shortest distance between `word1` and `word2` in the array `wordsDict`.

**Example 1:**
```
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding"); // return 1
```

**Constraints:**
- `1 <= wordsDict.length <= 3 * 10^4`
- `1 <= wordsDict[i].length <= 10`
- `wordsDict[i]` consists of lowercase English letters.
- `word1` and `word2` are in `wordsDict`.
- `word1 != word2`
- At most `5000` calls will be made to `shortest`.

## My Approach

I used a **Design Pattern** with hash map preprocessing to optimize multiple queries. The key insight is to preprocess the word indices in the constructor and reuse them for all queries.

**Algorithm:**
1. **Constructor:** Build hash map of word indices during initialization
2. **Shortest Method:** Use two pointers on precomputed indices
   - Get indices for word1 and word2
   - Use two-pointer approach to find minimum distance
   - Return minimum distance found

## Solution

The solution uses design pattern with hash map preprocessing for efficient multiple queries. See the implementation in the [solution file](../exercises/244.shortest-word-distance-ii.py).

**Key Points:**
- Preprocesses word indices in constructor
- Reuses hash map for all queries
- Two-pointer approach for distance calculation
- Optimized for multiple queries

## Time & Space Complexity

**Constructor Time:** O(n)
- Build hash map: O(n)

**Shortest Method Time:** O(m + k)
- m, k are occurrences of word1, word2
- Two-pointer traversal: O(m + k)

**Space Complexity:** O(n)
- Hash map stores indices for all words
- Total: O(n)

## Key Insights

1. **Preprocessing:** Building hash map in constructor optimizes multiple queries.

2. **Design Pattern:** Using class design allows efficient reuse of precomputed data.

3. **Two Pointers:** Two-pointer approach on sorted indices is optimal.

4. **Multiple Queries:** Preprocessing pays off when many queries are made.

5. **Index Reuse:** Same indices can be used for different word pairs.

6. **Efficient Lookup:** Hash map provides O(1) lookup for word indices.

## Mistakes Made

1. **No Preprocessing:** Initially might rebuild indices for each query.

2. **Wrong Design:** Not using class design for multiple queries.

3. **Inefficient Approach:** Using O(n) approach for each query.

4. **Complex Logic:** Overcomplicating the distance calculation.

## Related Problems

- **Shortest Word Distance** (Problem 243): Single query version
- **Shortest Word Distance III** (Problem 245): Handle same word case
- **Design HashMap** (Problem 706): Design hash map data structure
- **Design HashSet** (Problem 705): Design hash set data structure

## Alternative Approaches

1. **Lazy Loading:** Build indices only when first queried
2. **Binary Search:** Use binary search on sorted indices
3. **Caching:** Cache results for repeated queries

## Common Pitfalls

1. **No Preprocessing:** Rebuilding indices for each query.
2. **Wrong Design:** Not using class design for multiple queries.
3. **Inefficient Approach:** Using O(n) approach for each query.
4. **Memory Issues:** Not considering space complexity of preprocessing.
5. **Complex Logic:** Overcomplicating the distance calculation.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/244.shortest-word-distance-ii.py)](../exercises/244.shortest-word-distance-ii.py)

*Note: This is a design problem that demonstrates efficient preprocessing for multiple queries.*
