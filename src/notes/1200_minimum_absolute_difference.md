# Minimum Absolute Difference

[![Problem 1200](https://img.shields.io/badge/Problem-1200-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/minimum-absolute-difference/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/minimum-absolute-difference/)

**Problem Number:** [1200](https://leetcode.com/problems/minimum-absolute-difference/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Sorting
**LeetCode Link:** [https://leetcode.com/problems/minimum-absolute-difference/](https://leetcode.com/problems/minimum-absolute-difference/)

## Problem Description

Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order (with respect to pairs), each pair `[a, b]` follows

- `a, b` are from `arr`
- `a < b`
- `b - a` equals the minimum absolute difference of any two elements in `arr`

**Example 1:**
```
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
```

**Example 2:**
```
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Explanation: The minimum absolute difference is 2.
```

**Example 3:**
```
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
```

**Constraints:**
- `2 <= arr.length <= 10^5`
- `-10^6 <= arr[i] <= 10^6`

## My Approach

I used a **Sorting** approach to find the minimum absolute difference efficiently. The key insight is that the minimum absolute difference must occur between adjacent elements in the sorted array.

**Algorithm:**
1. Sort the array in ascending order
2. Initialize minimum absolute difference to infinity
3. Iterate through adjacent pairs in the sorted array
4. Calculate absolute difference between each pair
5. If current difference is smaller than minimum, update minimum and reset result list
6. If current difference equals minimum, add the pair to result list
7. Return all pairs with minimum absolute difference

## Solution

The solution uses sorting to find minimum absolute differences efficiently. See the implementation in the [solution file](../exercises/1200.minimum-absolute-difference.py).

**Key Points:**
- Sorts array to ensure adjacent elements have minimum differences
- Tracks minimum absolute difference found so far
- Collects all pairs with the minimum difference
- Returns pairs in ascending order as required
- Handles multiple pairs with same minimum difference

## Time & Space Complexity

**Time Complexity:** O(n log n)
- Sorting: O(n log n)
- Single pass through sorted array: O(n)
- Total: O(n log n)

**Space Complexity:** O(n)
- Result list can contain up to n/2 pairs
- Each pair contains 2 elements
- Total: O(n)

## Key Insights

1. **Sorting Advantage:** After sorting, the minimum absolute difference must occur between adjacent elements.

2. **Adjacent Pairs:** We only need to check consecutive elements in the sorted array, not all possible pairs.

3. **Multiple Minimums:** There can be multiple pairs with the same minimum absolute difference.

4. **Efficient Tracking:** We can track the minimum difference and collect all pairs with that difference in one pass.

5. **Ordered Output:** The sorted array naturally provides pairs in ascending order.

6. **Distinct Elements:** Since all elements are distinct, we don't need to handle duplicates.

## Mistakes Made

1. **Brute Force:** Initially might check all possible pairs, leading to O(n²) complexity.

2. **Wrong Order:** Not sorting the array first, missing the adjacent pair insight.

3. **Complex Logic:** Overcomplicating the minimum tracking logic.

4. **Missing Pairs:** Not collecting all pairs with the same minimum difference.

## Related Problems

- **Two Sum** (Problem 1): Find pairs that sum to target
- **3Sum** (Problem 15): Find triplets that sum to zero
- **Closest 3Sum** (Problem 16): Find triplet closest to target
- **Two Sum II** (Problem 167): Two sum in sorted array

## Alternative Approaches

1. **Hash Set:** Use hash set to track seen differences - O(n²) time complexity
2. **Two Pointers:** Use two pointers on sorted array - O(n log n) time
3. **Priority Queue:** Use min-heap to track differences - O(n log n) time

## Common Pitfalls

1. **Brute Force:** Checking all possible pairs instead of using sorting.
2. **Wrong Order:** Not sorting the array to find adjacent minimum differences.
3. **Missing Pairs:** Not collecting all pairs with the same minimum difference.
4. **Complex Logic:** Overcomplicating the minimum tracking.
5. **Order Issues:** Not returning pairs in the required ascending order.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/1200.minimum-absolute-difference.py)](../exercises/1200.minimum-absolute-difference.py)

*Note: This is a simple sorting problem that demonstrates efficient finding of minimum differences between adjacent elements.*
