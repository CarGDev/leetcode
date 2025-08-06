# Partition Array Such That Maximum Difference Is K

[![Problem 2294](https://img.shields.io/badge/Problem-2294-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/)

**Problem Number:** [2294](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Greedy, Sorting
**LeetCode Link:** [https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/)

## Problem Description

You are given an integer array `nums` and an integer `k`. You may partition `nums` into one or more **subsequences** such that each element in `nums` appears in **exactly one** of the subsequences.

Let the **maximum difference** of a subsequence be the difference between the **maximum** and **minimum** element in the subsequence.

Return *the **minimum** number of subsequences needed so that the maximum difference of each subsequence is **at most*** `k`.

**Example 1:**
```
Input: nums = [3,6,1,2,5], k = 2
Output: 2
Explanation:
We can partition nums into the two subsequences [3,1,2] and [6,5].
- The maximum difference of the first subsequence is 3 - 1 = 2.
- The maximum difference of the second subsequence is 6 - 5 = 1.
Both subsequences have a maximum difference of at most 2, so we return 2.
```

**Example 2:**
```
Input: nums = [1,2,3], k = 1
Output: 2
Explanation:
We can partition nums into the two subsequences [1,2] and [3].
- The maximum difference of the first subsequence is 2 - 1 = 1.
- The maximum difference of the second subsequence is 3 - 3 = 0.
Both subsequences have a maximum difference of at most 1, so we return 2.
```

**Example 3:**
```
Input: nums = [2,2,4,5], k = 0
Output: 3
Explanation:
We can partition nums into the three subsequences [2], [2], and [4,5].
- The maximum difference of the first subsequence is 2 - 2 = 0.
- The maximum difference of the second subsequence is 2 - 2 = 0.
- The maximum difference of the third subsequence is 5 - 4 = 1.
All subsequences have a maximum difference of at most 0, so we return 3.
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `0 <= k <= 10^5`

## My Approach

I used a **Greedy** approach with sorting to find the minimum number of subsequences. The key insight is to sort the unique elements and group them into subsequences where the maximum difference is at most k.

**Algorithm:**
1. Handle edge case: if k == 0, return number of unique elements
2. Remove duplicates and sort the array
3. Initialize minimum value and subsequence count
4. For each element:
   - Update minimum value if current element is smaller
   - Calculate difference between current element and minimum
   - If difference > k, increment subsequence count and reset minimum
5. Return total number of subsequences

## Solution

The solution uses greedy approach with sorting to minimize subsequences. See the implementation in the [solution file](../exercises/2294.partition-array-such-that-maximum-difference-is-k.py).

**Key Points:**
- Removes duplicates and sorts array
- Uses greedy approach to group elements
- Tracks minimum value in current subsequence
- Increments count when difference exceeds k
- Handles edge case when k == 0

## Time & Space Complexity

**Time Complexity:** O(n log n)
- Sorting: O(n log n)
- Single pass through sorted array: O(n)
- Total: O(n log n)

**Space Complexity:** O(n)
- Set to remove duplicates: O(n)
- Sorted list: O(n)
- Total: O(n)

## Key Insights

1. **Sorting:** Sorting allows us to process elements in order and group them efficiently.

2. **Greedy Approach:** Always start a new subsequence when the difference exceeds k.

3. **Duplicate Removal:** Removing duplicates simplifies the problem.

4. **Minimum Tracking:** Track the minimum value in the current subsequence.

5. **Edge Case:** When k == 0, each unique element needs its own subsequence.

6. **Difference Calculation:** Calculate difference between current element and minimum in subsequence.

## Mistakes Made

1. **Wrong Order:** Not sorting the array, leading to incorrect grouping.

2. **Complex Logic:** Overcomplicating the subsequence grouping.

3. **Missing Edge Case:** Not handling k == 0 case properly.

4. **Wrong Counting:** Not correctly counting subsequences.

## Related Problems

- **Partition Labels** (Problem 763): Partition string into labels
- **Partition Equal Subset Sum** (Problem 416): Partition array into equal sums
- **Partition to K Equal Sum Subsets** (Problem 698): Partition into k equal subsets
- **Minimum Absolute Difference** (Problem 1200): Find minimum absolute difference

## Alternative Approaches

1. **Dynamic Programming:** Use DP to find optimal partitioning - O(n²) time
2. **Binary Search:** Use binary search on number of subsequences - O(n log n) time
3. **Two Pointers:** Use two pointers to find valid ranges - O(n log n) time

## Common Pitfalls

1. **Wrong Order:** Not sorting the array for efficient grouping.
2. **Complex Logic:** Overcomplicating the subsequence grouping logic.
3. **Missing Edge Case:** Not handling k == 0 case properly.
4. **Wrong Counting:** Not correctly counting the number of subsequences.
5. **Inefficient Approach:** Using brute force when greedy approach suffices.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/2294.partition-array-such-that-maximum-difference-is-k.py)](../exercises/2294.partition-array-such-that-maximum-difference-is-k.py)

*Note: This is a greedy problem that demonstrates efficient array partitioning with difference constraints.*
