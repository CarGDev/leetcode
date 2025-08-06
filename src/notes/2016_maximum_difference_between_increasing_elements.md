# Maximum Difference Between Increasing Elements

[![Problem 2016](https://img.shields.io/badge/Problem-2016-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)

**Problem Number:** [2016](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Greedy
**LeetCode Link:** [https://leetcode.com/problems/maximum-difference-between-increasing-elements/](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)

## Problem Description

Given a **0-indexed** integer array `nums` of size `n`, find the **maximum difference** between `nums[i]` and `nums[j]` (i.e., `nums[j] - nums[i]`), such that `0 <= i < j < n` and `nums[i] < nums[j]`.

Return the **maximum difference**. If no such `i` and `j` exists, return `-1`.

**Example 1:**
```
Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 3, the difference nums[j] - nums[i] = 4 - 1 = 3, but it is not the maximum difference.
```

**Example 2:**
```
Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].
```

**Example 3:**
```
Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
```

**Constraints:**
- `n == nums.length`
- `2 <= n <= 1000`
- `1 <= nums[i] <= 10^9`

## My Approach

I used a **Brute Force** approach to find the maximum difference. The key insight is to check all possible pairs (i, j) where i < j and nums[i] < nums[j].

**Algorithm:**
1. Initialize maximum difference to -1
2. For each index i from 0 to n-2:
   - For each index j from i+1 to n-1:
     - If nums[i] < nums[j], calculate difference
     - Update maximum difference if current difference is larger
3. Return the maximum difference found

## Solution

The solution uses brute force to check all valid pairs. See the implementation in the [solution file](../exercises/2016.maximum-difference-between-increasing-elements.py).

**Key Points:**
- Checks all possible pairs (i, j) where i < j
- Only considers pairs where nums[i] < nums[j]
- Tracks maximum difference found
- Returns -1 if no valid pair exists

## Time & Space Complexity

**Time Complexity:** O(n²)
- Nested loops: outer loop O(n), inner loop O(n)
- Each iteration performs constant time operations
- Total: O(n²)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Brute Force:** Checking all possible pairs is straightforward for this problem.

2. **Valid Pairs:** Only consider pairs where i < j and nums[i] < nums[j].

3. **Maximum Tracking:** Keep track of the maximum difference found so far.

4. **Return Value:** Return -1 if no valid pair exists.

5. **0-Indexed:** The problem uses 0-indexed arrays.

6. **Simple Logic:** The solution logic is straightforward and easy to understand.

## Mistakes Made

1. **Wrong Order:** Initially might check pairs where i > j.

2. **Missing Condition:** Not checking nums[i] < nums[j] condition.

3. **Complex Logic:** Overcomplicating the pair checking logic.

4. **Wrong Return:** Not returning -1 when no valid pair exists.

## Related Problems

- **Best Time to Buy and Sell Stock** (Problem 121): Find maximum profit
- **Best Time to Buy and Sell Stock II** (Problem 122): Multiple transactions
- **Container With Most Water** (Problem 11): Find maximum area
- **Trapping Rain Water** (Problem 42): Calculate trapped water

## Alternative Approaches

1. **Single Pass:** Track minimum element and calculate differences - O(n) time
2. **Two Pointers:** Use two pointers for optimization - O(n) time
3. **Dynamic Programming:** Use DP to track maximum differences - O(n) time

## Common Pitfalls

1. **Wrong Order:** Checking pairs where i > j.
2. **Missing Condition:** Not verifying nums[i] < nums[j].
3. **Complex Logic:** Overcomplicating the pair checking.
4. **Wrong Return:** Not handling the case where no valid pair exists.
5. **Inefficient Approach:** Using O(n²) when O(n) is possible.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/2016.maximum-difference-between-increasing-elements.py)](../exercises/2016.maximum-difference-between-increasing-elements.py)

*Note: This is a simple array problem that demonstrates brute force approach for finding maximum differences.*
