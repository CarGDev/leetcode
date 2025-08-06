# Subsets II

[![Problem 90](https://img.shields.io/badge/Problem-90-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/subsets-ii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/subsets-ii/)

**Problem Number:** [90](https://leetcode.com/problems/subsets-ii/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Backtracking
**LeetCode Link:** [https://leetcode.com/problems/subsets-ii/](https://leetcode.com/problems/subsets-ii/)

## Problem Description

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

**Example 1:**
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2:**
```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## My Approach

I used a **Backtracking** approach with duplicate handling. The key insight is to sort the array first and then use backtracking while skipping duplicates at the same level to avoid generating duplicate subsets.

**Algorithm:**
1. Sort the input array to group duplicates together
2. Use backtracking with a helper function
3. For each recursive call, add the current path to result
4. Iterate through remaining elements starting from current position
5. Skip duplicates at the same level (i > start and nums[i] == nums[i-1])
6. Add current element to path, recurse, then remove (backtrack)

## Solution

The solution uses backtracking with duplicate handling. See the implementation in the [solution file](../exercises/90.subsets-ii.py).

**Key Points:**
- Sorts array to group duplicates together
- Uses backtracking to generate all subsets
- Skips duplicates at the same recursion level
- Adds each valid subset to the result
- Handles empty subset and all possible combinations

## Time & Space Complexity

**Time Complexity:** O(n × 2^n)
- Sorting: O(n log n)
- Backtracking generates 2^n subsets
- Each subset can be up to length n
- Total: O(n × 2^n)

**Space Complexity:** O(n)
- Recursion stack depth: O(n)
- Path array: O(n)
- Result space: O(2^n) for storing all subsets

## Key Insights

1. **Sorting for Duplicates:** Sorting groups duplicates together, making it easier to skip them.

2. **Duplicate Skipping:** We skip duplicates at the same recursion level (i > start) to avoid generating duplicate subsets.

3. **Backtracking Pattern:** This is a classic backtracking problem where we build subsets incrementally.

4. **Level-based Duplicate Handling:** We only skip duplicates at the same level, not across different levels.

5. **Path Copying:** We copy the current path (path[:]) before adding to result to avoid reference issues.

6. **Empty Subset:** The empty subset is always included in the result.

## Mistakes Made

1. **No Sorting:** Initially might not sort the array, making duplicate handling complex.

2. **Wrong Duplicate Logic:** Skipping all duplicates instead of only at the same level.

3. **Reference Issues:** Not copying the path before adding to result.

4. **Complex Logic:** Overcomplicating the duplicate handling logic.

## Related Problems

- **Subsets** (Problem 78): Generate subsets without duplicates
- **Combinations** (Problem 77): Generate combinations of given length
- **Permutations II** (Problem 47): Generate permutations with duplicates
- **Combination Sum II** (Problem 40): Find combinations with duplicates

## Alternative Approaches

1. **Iterative:** Use iterative approach with bit manipulation - O(n × 2^n) time
2. **Hash Set:** Use hash set to track seen subsets - O(n × 2^n) time, O(2^n) space
3. **Recursive without Backtracking:** Use pure recursion approach

## Common Pitfalls

1. **No Sorting:** Not sorting the array to group duplicates.
2. **Wrong Duplicate Handling:** Skipping all duplicates instead of same-level duplicates.
3. **Reference Issues:** Not copying paths before adding to result.
4. **Complex Logic:** Overcomplicating the duplicate handling.
5. **Missing Empty Subset:** Not including the empty subset in the result.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/90.subsets-ii.py)](../exercises/90.subsets-ii.py)

*Note: This is a classic backtracking problem that demonstrates efficient handling of duplicates in subset generation.*
