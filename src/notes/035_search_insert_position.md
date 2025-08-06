# Search Insert Position

[![Problem 35](https://img.shields.io/badge/Problem-35-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/search-insert-position/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/search-insert-position/)

**Problem Number:** [35](https://leetcode.com/problems/search-insert-position/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Binary Search
**LeetCode Link:** [https://leetcode.com/problems/search-insert-position/](https://leetcode.com/problems/search-insert-position/)

## Problem Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order
- `-10^4 <= target <= 10^4`

## My Approach

I used a **Binary Search** approach with optimization for edge cases. The key insight is to use binary search to find the target or determine where it should be inserted, with special handling for targets larger than the maximum element.

**Algorithm:**
1. Handle edge case: if target > last element, return array length
2. Use binary search with left and right pointers
3. When target > mid element, search right half (left = mid + 1)
4. When target ≤ mid element, search left half (right = mid)
5. Return left pointer when search converges

## Solution

The solution uses binary search with edge case optimization. See the implementation in the [solution file](../exercises/35.search-insert-position.py).

**Key Points:**
- Uses binary search for O(log n) time complexity
- Handles edge case where target is larger than all elements
- Returns insertion position when target is not found
- Maintains sorted order requirement
- Efficiently narrows search space

## Time & Space Complexity

**Time Complexity:** O(log n)
- Binary search halves the search space in each iteration
- Total iterations: log₂(n)
- Total: O(log n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Binary Search Efficiency:** Binary search provides the required O(log n) time complexity for sorted arrays.

2. **Edge Case Handling:** When target is larger than the maximum element, it should be inserted at the end (index = array length).

3. **Insertion Position:** When target is not found, the left pointer naturally points to the correct insertion position.

4. **Sorted Array Advantage:** The sorted nature of the array enables efficient binary search.

5. **Convergence:** The binary search converges to the correct insertion position even when the target is not found.

6. **Distinct Values:** The problem guarantees distinct values, simplifying the comparison logic.

## Mistakes Made

1. **Linear Search:** Initially might use linear search, which doesn't meet the O(log n) requirement.

2. **Wrong Edge Case:** Not properly handling the case where target is larger than all elements.

3. **Complex Logic:** Overcomplicating the binary search with unnecessary conditions.

4. **Return Value Confusion:** Not understanding that the left pointer gives the insertion position.

## Related Problems

- **Binary Search** (Problem 704): Basic binary search implementation
- **Find First and Last Position of Element in Sorted Array** (Problem 34): Binary search with duplicates
- **Search in Rotated Sorted Array** (Problem 33): Binary search in modified sorted array
- **Find Peak Element** (Problem 162): Binary search for peak finding

## Alternative Approaches

1. **Linear Search:** Check each element sequentially - O(n) time complexity
2. **Built-in Functions:** Use bisect.bisect_left() in Python
3. **Recursive Binary Search:** Use recursion instead of iteration

## Common Pitfalls

1. **Wrong Complexity:** Using linear search instead of binary search.
2. **Edge Case Handling:** Not handling targets larger than the maximum element.
3. **Binary Search Logic:** Incorrectly implementing the binary search algorithm.
4. **Return Value:** Not understanding what the left pointer represents.
5. **Over-engineering:** Adding unnecessary complexity to a straightforward binary search.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/35.search-insert-position.py)](../exercises/35.search-insert-position.py)

*Note: This is a fundamental binary search problem that demonstrates how to find insertion positions in sorted arrays efficiently.*
