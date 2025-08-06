# Summary Ranges

[![Problem 228](https://img.shields.io/badge/Problem-228-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/summary-ranges/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/summary-ranges/)

**Problem Number:** [228](https://leetcode.com/problems/summary-ranges/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array
**LeetCode Link:** [https://leetcode.com/problems/summary-ranges/](https://leetcode.com/problems/summary-ranges/)

## Problem Description

You are given a **sorted unique** integer array `nums`.

A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the **smallest sorted** list of ranges that **cover all the numbers in the array exactly**. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

**Example 1:**
```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

**Example 2:**
```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

**Constraints:**
- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- All the values of `nums` are unique.
- `nums` is sorted in ascending order.

## My Approach

I used a **Two Pointers** approach to identify consecutive ranges. The key insight is to use two pointers (i, j) to track the start and end of each consecutive range.

**Algorithm:**
1. Handle edge cases (empty array, single element)
2. Initialize two pointers i and j at start
3. Iterate through array starting from second element
4. If current element is consecutive (nums[h-1] + 1 == nums[h]), extend range
5. Otherwise, add current range to result and reset pointers
6. Handle the last range after loop ends
7. Return list of formatted ranges

## Solution

The solution uses two pointers to identify and format consecutive ranges. See the implementation in the [solution file](../exercises/228.summary-ranges.py).

**Key Points:**
- Uses two pointers to track range boundaries
- Handles single element ranges (i == j)
- Formats ranges as "a->b" or "a"
- Handles edge cases properly
- Processes last range after loop

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through the array
- Each element is processed once
- Total: O(n)

**Space Complexity:** O(n)
- Result list can contain up to n ranges
- Each range is a string
- Total: O(n)

## Key Insights

1. **Two Pointers:** Using i and j pointers to track range boundaries.

2. **Consecutive Check:** Checking if nums[h-1] + 1 == nums[h] for consecutive elements.

3. **Range Formatting:** Single element ranges are formatted as "a", multiple elements as "a->b".

4. **Edge Cases:** Handling empty arrays and single element arrays.

5. **Last Range:** Processing the last range after the loop ends.

6. **Sorted Input:** Leveraging the fact that input is sorted.

## Mistakes Made

1. **Wrong Range Logic:** Initially might use wrong logic for identifying ranges.

2. **Missing Edge Cases:** Not handling empty arrays or single elements properly.

3. **Wrong Formatting:** Not formatting ranges correctly.

4. **Last Range:** Forgetting to process the last range after the loop.

## Related Problems

- **Merge Intervals** (Problem 56): Merge overlapping intervals
- **Insert Interval** (Problem 57): Insert new interval into sorted intervals
- **Missing Ranges** (Problem 163): Find missing ranges
- **Range Sum Query** (Problem 303): Calculate sum in range

## Alternative Approaches

1. **Single Pointer:** Use single pointer with range tracking - O(n) time
2. **Stack-based:** Use stack to track ranges - O(n) time, O(n) space
3. **Recursive:** Use recursion to process ranges - O(n) time, O(n) space

## Common Pitfalls

1. **Wrong Range Logic:** Using incorrect logic for identifying consecutive ranges.
2. **Missing Edge Cases:** Not handling empty arrays or single elements.
3. **Wrong Formatting:** Not formatting ranges correctly.
4. **Last Range:** Forgetting to process the last range after the loop.
5. **Complex Logic:** Overcomplicating the range identification.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/228.summary-ranges.py)](../exercises/228.summary-ranges.py)

*Note: This is a range processing problem that demonstrates efficient consecutive range identification with two pointers.*
