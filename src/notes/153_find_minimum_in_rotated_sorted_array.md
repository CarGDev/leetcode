# Find Minimum in Rotated Sorted Array

[![Problem 153](https://img.shields.io/badge/Problem-153-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

**Problem Number:** [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Binary Search
**LeetCode Link:** [https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Problem Description

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

**Example 3:**
```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

**Constraints:**
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are unique.
- `nums` is sorted and rotated between `1` and `n` times.

## My Approach

I used **Binary Search** to find the minimum element efficiently. The key insight is that in a rotated sorted array, the minimum element is always in the unsorted half.

**Algorithm:**
1. Initialize left and right pointers
2. While left <= right:
   - If left == right, return the element (single element case)
   - Calculate middle index
   - If middle element > right element, minimum is in right half
   - Otherwise, minimum is in left half (including middle)
3. Return the minimum element

## Solution

The solution uses binary search to find the minimum element in O(log n) time. See the implementation in the [solution file](../exercises/153.find-minimum-in-rotated-sorted-array.py).

**Key Points:**
- Uses binary search for O(log n) time complexity
- Compares middle element with right element to determine search direction
- Handles single element case when left == right
- Returns minimum element efficiently

## Time & Space Complexity

**Time Complexity:** O(log n)
- Binary search halves the search space each iteration
- Each iteration performs constant time operations
- Total: O(log n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Binary Search:** Using binary search achieves the required O(log n) time complexity.

2. **Rotation Property:** In a rotated sorted array, the minimum is always in the unsorted half.

3. **Comparison Strategy:** Comparing middle element with right element determines which half to search.

4. **Single Element Case:** When left == right, we've found the minimum element.

5. **Unique Elements:** The problem guarantees unique elements, simplifying the logic.

6. **Sorted Property:** Despite rotation, the array maintains sorted properties that enable binary search.

## Mistakes Made

1. **Linear Search:** Initially might use linear search, leading to O(n) complexity.

2. **Wrong Comparison:** Not using the correct comparison strategy for rotated arrays.

3. **Complex Logic:** Overcomplicating the binary search implementation.

4. **Edge Cases:** Not properly handling single element or edge cases.

## Related Problems

- **Search in Rotated Sorted Array** (Problem 33): Search target in rotated array
- **Search in Rotated Sorted Array II** (Problem 81): Search with duplicates
- **Find Peak Element** (Problem 162): Find peak in array
- **Binary Search** (Problem 704): Standard binary search

## Alternative Approaches

1. **Linear Search:** Check each element - O(n) time, O(1) space
2. **Recursive Binary Search:** Use recursion for binary search - O(log n) time, O(log n) space
3. **Two Pointers:** Use two pointers to find rotation point - O(log n) time

## Common Pitfalls

1. **Linear Search:** Using linear search instead of binary search.
2. **Wrong Comparison:** Not using the correct comparison strategy for rotated arrays.
3. **Complex Implementation:** Overcomplicating the binary search logic.
4. **Edge Cases:** Not handling single element or edge cases properly.
5. **Time Complexity:** Not achieving the required O(log n) time complexity.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/153.find-minimum-in-rotated-sorted-array.py)](../exercises/153.find-minimum-in-rotated-sorted-array.py)

*Note: This is a binary search problem that demonstrates efficient minimum finding in rotated sorted arrays.*
