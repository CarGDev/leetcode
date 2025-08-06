# H-Index

[![Problem 274](https://img.shields.io/badge/Problem-274-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/h-index/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/h-index/)

**Problem Number:** [274](https://leetcode.com/problems/h-index/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Sorting, Counting Sort
**LeetCode Link:** [https://leetcode.com/problems/h-index/](https://leetcode.com/problems/h-index/)

## Problem Description

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i^th` paper, return *compute the researcher's* `h-index`.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): A scientist has an index `h` if `h` of their `n` papers have at least `h` citations each, and the other `n − h` papers have no more than `h` citations each.

If there are several possible values for `h`, the maximum one is taken as the `h-index`.

**Example 1:**
```
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
```

**Example 2:**
```
Input: citations = [1,3,1]
Output: 1
```

**Constraints:**
- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

## My Approach

I used a **Sorting** approach to find the h-index. The key insight is to sort the citations in ascending order and find the largest h where at least h papers have h or more citations.

**Algorithm:**
1. Sort citations in ascending order
2. Iterate through sorted citations
3. For each position i, check if citations[i] >= (n - i)
4. Return (n - i) when condition is met
5. Return 0 if no h-index found

## Solution

The solution uses sorting to efficiently find the h-index. See the implementation in the [solution file](../exercises/274.h-index.py).

**Key Points:**
- Sorts citations in ascending order
- Checks h-index condition for each position
- Returns maximum valid h-index
- Handles edge cases properly

## Time & Space Complexity

**Time Complexity:** O(n log n)
- Sorting: O(n log n)
- Single pass through sorted array: O(n)
- Total: O(n log n)

**Space Complexity:** O(1)
- In-place sorting (modifies input)
- Uses only constant extra space

## Key Insights

1. **Sorting:** Sorting allows efficient h-index calculation.

2. **H-index Condition:** At position i, h-index is (n - i) if citations[i] >= (n - i).

3. **Maximum H-index:** Return the first valid h-index found (largest possible).

4. **Position Logic:** After sorting, position i represents (n - i) papers with >= citations[i].

5. **Edge Cases:** Return 0 if no valid h-index found.

6. **Efficient Check:** Single pass through sorted array is sufficient.

## Mistakes Made

1. **Wrong Order:** Initially might sort in descending order.

2. **Complex Logic:** Overcomplicating the h-index calculation.

3. **Wrong Condition:** Not understanding the h-index condition properly.

4. **Inefficient Approach:** Using O(n²) approach when sorting suffices.

## Related Problems

- **H-Index II** (Problem 275): H-index with sorted citations
- **Sort Colors** (Problem 75): Three-way partitioning
- **Kth Largest Element** (Problem 215): Find kth largest element
- **Top K Frequent Elements** (Problem 347): Find most frequent elements

## Alternative Approaches

1. **Counting Sort:** Use counting sort for O(n) time - O(n) space
2. **Binary Search:** Use binary search on h-index values - O(n log n) time
3. **Bucket Sort:** Use bucket sort for O(n) time - O(n) space

## Common Pitfalls

1. **Wrong Order:** Sorting in wrong order.
2. **Complex Logic:** Overcomplicating the h-index calculation.
3. **Wrong Condition:** Not understanding the h-index condition.
4. **Inefficient Approach:** Using O(n²) approach when sorting suffices.
5. **Edge Cases:** Not handling cases where no h-index exists.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/274.h-index.py)](../exercises/274.h-index.py)

*Note: This is a sorting problem that demonstrates efficient h-index calculation with position-based logic.*
