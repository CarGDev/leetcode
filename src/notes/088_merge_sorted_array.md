# Merge Sorted Array

[![Problem 88](https://img.shields.io/badge/Problem-88-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/merge-sorted-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/merge-sorted-array/)

**Problem Number:** [88](https://leetcode.com/problems/merge-sorted-array/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Two Pointers, Sorting
**LeetCode Link:** [https://leetcode.com/problems/merge-sorted-array/](https://leetcode.com/problems/merge-sorted-array/)

## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**Example 1:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

**Example 2:**
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

**Example 3:**
```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

**Constraints:**
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## My Approach

I used a **Simple Merge** approach by copying elements from nums2 to the end of nums1, then sorting the entire array. The key insight is to utilize the extra space at the end of nums1 to merge the arrays.

**Algorithm:**
1. Copy all elements from nums2 to the end of nums1 (starting from index m)
2. Sort the entire nums1 array to get the final merged result
3. The merged result is stored in-place in nums1

## Solution

The solution uses a simple merge approach with sorting. See the implementation in the [solution file](../exercises/88.merge-sorted-array.py).

**Key Points:**
- Copies nums2 elements to the end of nums1
- Uses built-in sort to merge the arrays
- Modifies nums1 in-place as required
- Handles edge cases like empty arrays
- Simple and straightforward approach

## Time & Space Complexity

**Time Complexity:** O((m+n) log(m+n))
- Copying elements: O(n)
- Sorting: O((m+n) log(m+n))
- Total: O((m+n) log(m+n))

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- Modifies nums1 in-place
- No additional data structures needed

## Key Insights

1. **Extra Space Utilization:** nums1 has extra space at the end that can be used for merging.

2. **Simple Approach:** Copying nums2 to nums1 and then sorting is straightforward and works correctly.

3. **In-Place Modification:** The problem requires modifying nums1 in-place, which this approach does.

4. **Built-in Sort:** Using the built-in sort function ensures correct ordering.

5. **Edge Case Handling:** The approach naturally handles cases where one array is empty.

6. **Space Efficiency:** No additional arrays are needed, just the existing space in nums1.

## Mistakes Made

1. **Complex Merge Logic:** Initially might try to implement complex merge logic with two pointers.

2. **Wrong Indexing:** Not properly handling the indices when copying elements.

3. **Sorting Issues:** Not understanding that sorting after copying is a valid approach.

4. **Return Value:** Trying to return the array when the function should modify nums1 in-place.

## Related Problems

- **Merge Two Sorted Lists** (Problem 21): Merge two sorted linked lists
- **Merge k Sorted Lists** (Problem 23): Merge multiple sorted linked lists
- **Sort Colors** (Problem 75): Sort array with three colors
- **Remove Duplicates from Sorted Array** (Problem 26): Remove duplicates in sorted array

## Alternative Approaches

1. **Two Pointer Merge:** Use two pointers to merge from end to beginning - O(m+n) time, O(1) space
2. **Three Pointer Merge:** Use three pointers for more efficient merging
3. **Built-in Merge:** Use heapq.merge() for efficient merging (though not in-place)

## Common Pitfalls

1. **Complex Implementation:** Overcomplicating the merge logic when simple approach works.
2. **Wrong Indices:** Not properly handling array indices when copying elements.
3. **Return Value:** Trying to return the array instead of modifying in-place.
4. **Space Usage:** Using additional arrays when in-place modification is required.
5. **Sorting Neglect:** Not understanding that sorting after copying is acceptable.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/88.merge-sorted-array.py)](../exercises/88.merge-sorted-array.py)

*Note: This is a fundamental array manipulation problem that demonstrates simple merging with sorting.*
