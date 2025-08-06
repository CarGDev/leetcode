# Median of Two Sorted Arrays

[![Problem 4](https://img.shields.io/badge/Problem-4-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/median-of-two-sorted-arrays/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=HARD)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/median-of-two-sorted-arrays/)

**Problem Number:** [4](https://leetcode.com/problems/median-of-two-sorted-arrays/)
**Difficulty:** [Hard](https://leetcode.com/problemset/?difficulty=HARD)
**Category:** Array, Binary Search, Divide and Conquer
**LeetCode Link:** [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n)).

**Example 1:**
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Constraints:**
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## My Approach

I used a **Binary Search** approach to find the correct partition of both arrays that gives us the median. The key insight is to find the correct cut point in the smaller array such that all elements on the left side are less than all elements on the right side.

**Algorithm:**
1. Ensure nums1 is the smaller array (swap if necessary)
2. Use binary search on the smaller array to find the correct partition
3. Calculate the corresponding partition in the larger array
4. Check if the partition is correct (left elements ≤ right elements)
5. Adjust the search range based on the comparison
6. Calculate median based on the correct partition

## Solution

The solution uses binary search to find the optimal partition point. See the implementation in the [solution file](../exercises/4.median-of-two-sorted-arrays.py).

**Key Points:**
- Uses binary search on the smaller array for efficiency
- Calculates corresponding partition in the larger array
- Handles edge cases with infinity values
- Supports both odd and even total lengths
- Achieves O(log(min(m,n))) time complexity

## Time & Space Complexity

**Time Complexity:** O(log(min(m, n)))
- Binary search on the smaller array
- Each iteration performs constant time operations
- Much better than O(m+n) merge approach

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Binary Search on Smaller Array:** Always perform binary search on the smaller array to minimize time complexity.

2. **Partition Concept:** The median divides the merged array into two equal halves, with all left elements ≤ all right elements.

3. **Cross-Array Validation:** After finding a partition in one array, validate it by checking the corresponding partition in the other array.

4. **Edge Case Handling:** Use infinity values to handle cases where partitions are at array boundaries.

5. **Odd vs Even Lengths:** Handle both cases - for odd total length, median is the minimum of right partition; for even, it's the average of max(left) and min(right).

6. **No Actual Merging:** The beauty of this approach is that we never actually merge the arrays.

## Mistakes Made

1. **Complexity Requirement:** Initially might consider O(m+n) merge approach, which doesn't meet the O(log(m+n)) requirement.

2. **Partition Logic:** Understanding the correct partition validation can be tricky initially.

3. **Edge Cases:** Handling cases where one array is empty or when partitions are at boundaries.

4. **Infinity Values:** Using appropriate infinity values for boundary conditions.

## Related Problems

- **Kth Smallest Element in Two Sorted Arrays:** Generalization of this problem
- **Merge k Sorted Lists** (Problem 23): Merging multiple sorted lists
- **Find First and Last Position of Element in Sorted Array** (Problem 34): Binary search applications
- **Search in Rotated Sorted Array** (Problem 33): Binary search in modified sorted arrays

## Alternative Approaches

1. **Merge and Find:** Merge arrays and find median - O(m+n) time, O(m+n) space
2. **Two Pointers:** Use two pointers to find median without merging - O(m+n) time, O(1) space
3. **Heap-based:** Use heaps to find kth smallest element - O((m+n)log(k)) time

## Common Pitfalls

1. **Wrong Complexity:** Not meeting the O(log(m+n)) requirement with merge approaches.
2. **Partition Validation:** Incorrectly validating the partition between arrays.
3. **Edge Cases:** Not handling empty arrays or single-element arrays properly.
4. **Infinity Handling:** Using wrong infinity values for boundary conditions.
5. **Odd/Even Logic:** Confusing the logic for odd vs even total lengths.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/4.median-of-two-sorted-arrays.py)](../exercises/4.median-of-two-sorted-arrays.py)

*Note: This is one of the most challenging binary search problems that requires deep understanding of partitioning and median properties.*
