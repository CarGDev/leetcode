# Remove Duplicates from Sorted Array II

[![Problem 80](https://img.shields.io/badge/Problem-80-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

**Problem Number:** [80](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some programming languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

**Example 1:**
```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1,1,2,2,3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0,0,1,1,2,3,3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order

## My Approach

I used a **Two Pointer** approach with a counter to track allowed duplicates. The key insight is to use a slow pointer to track the position where the next valid element should be placed, and allow at most two occurrences of each element.

**Algorithm:**
1. Handle edge cases (empty array or length <= 2)
2. Initialize slow pointer k at position 2 (first two elements are always valid)
3. Iterate through array starting from index 2
4. Check if current element is different from the two previous elements at k-1 and k-2
5. If different, copy current element to position k and increment k
6. Return k (number of elements in final array)

## Solution

The solution uses a two-pointer approach to allow at most two duplicates. See the implementation in the [solution file](../exercises/80.remove-duplicates-from-sorted-array-ii.py).

**Key Points:**
- Uses two pointers: slow pointer (k) and fast pointer (i)
- Allows at most two occurrences of each element
- Compares current element with two previous elements
- Modifies array in-place without extra space
- Returns count of elements in final array

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the array once
- Each iteration performs constant time operations
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- Modifies the array in-place
- No additional data structures needed

## Key Insights

1. **Two Pointer Technique:** Using a slow pointer to track the next position for valid elements.

2. **Duplicate Allowance:** We allow at most two occurrences of each element, not just one.

3. **Comparison Logic:** We compare the current element with the two previous elements at positions k-1 and k-2.

4. **In-Place Modification:** The problem requires modifying the array in-place, which is efficiently done with two pointers.

5. **Edge Case Handling:** Arrays with length <= 2 can be returned as-is since they can't have more than two duplicates.

6. **Sorted Array Advantage:** Since the array is sorted, duplicates are always adjacent, making the comparison simple.

## Mistakes Made

1. **Wrong Duplicate Count:** Initially might allow only one occurrence instead of two.

2. **Complex Logic:** Overcomplicating the comparison logic with unnecessary conditions.

3. **Wrong Pointer Logic:** Not properly understanding when to increment the slow pointer.

4. **Edge Case Missing:** Not properly handling arrays with length <= 2.

## Related Problems

- **Remove Duplicates from Sorted Array** (Problem 26): Remove all duplicates
- **Remove Element** (Problem 27): Remove specific element
- **Move Zeroes** (Problem 283): Move zeros to end
- **Sort Colors** (Problem 75): Sort array with three colors

## Alternative Approaches

1. **Hash Table:** Use hash table to count occurrences - O(n) time, O(n) space
2. **Three Pointers:** Use three pointers to track current and two previous elements
3. **Counter-based:** Use a counter to track occurrences of each element

## Common Pitfalls

1. **Wrong Duplicate Limit:** Allowing only one occurrence instead of two.
2. **Complex Comparison:** Overcomplicating the comparison logic.
3. **Wrong Pointer Movement:** Not properly understanding when to move the slow pointer.
4. **Edge Cases:** Not handling arrays with length <= 2.
5. **Extra Space:** Using additional data structures when in-place modification is required.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/80.remove-duplicates-from-sorted-array-ii.py)](../exercises/80.remove-duplicates-from-sorted-array-ii.py)

*Note: This is a variation of the classic two-pointer problem that demonstrates handling multiple allowed duplicates.*
