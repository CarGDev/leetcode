# Remove Element

[![Problem 27](https://img.shields.io/badge/Problem-27-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/remove-element/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/remove-element/)

**Problem Number:** [27](https://leetcode.com/problems/remove-element/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/remove-element/](https://leetcode.com/problems/remove-element/)

## Problem Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some programming languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

**Example 1:**
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,3,0,4,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the order of those five elements can be arbitrary.
```

**Constraints:**
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## My Approach

I used a **Two Pointer** approach with in-place modification. The key insight is to use a slow pointer to track the position where the next non-target element should be placed, and a fast pointer to scan through the array.

**Algorithm:**
1. Initialize slow pointer k at index 0
2. Iterate through array with fast pointer i
3. When nums[i] != val, copy nums[i] to nums[k] and increment k
4. Skip elements equal to val (don't copy them)
5. Return k (number of elements not equal to val)

## Solution

The solution uses a two-pointer approach for in-place element removal. See the implementation in the [solution file](../exercises/27.remove-element.py).

**Key Points:**
- Uses two pointers: slow pointer (k) and fast pointer (i)
- Modifies array in-place without extra space
- Copies only non-target elements to the front
- Returns count of elements not equal to val
- Maintains relative order of non-target elements

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the array once with the fast pointer
- Each element is checked and potentially copied once
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- Modifies the array in-place
- No additional data structures needed

## Key Insights

1. **Two Pointer Technique:** Using a slow pointer to track the next position for non-target elements and a fast pointer to scan through the array.

2. **In-Place Modification:** The problem requires modifying the array in-place, which is efficiently done with two pointers.

3. **Selective Copying:** We only copy elements that are not equal to the target value, effectively removing all occurrences.

4. **Order Preservation:** The two-pointer approach preserves the relative order of non-target elements.

5. **Efficient Skipping:** We skip target elements without copying them, minimizing unnecessary operations.

6. **Return Value:** The function returns the count of elements not equal to the target value.

## Mistakes Made

1. **Extra Space Usage:** Initially might use a new array or list to store non-target elements.

2. **Wrong Pointer Logic:** Not properly understanding when to increment the slow pointer.

3. **Inefficient Approach:** Using remove() or similar methods that shift elements.

4. **Return Value Confusion:** Returning the wrong value or not understanding what k represents.

## Related Problems

- **Remove Duplicates from Sorted Array** (Problem 26): Remove duplicates in sorted array
- **Move Zeroes** (Problem 283): Move all zeros to the end while maintaining order
- **Sort Colors** (Problem 75): Sort array with only 0, 1, 2 values
- **Remove Duplicates from Sorted Array II** (Problem 80): Allow at most 2 occurrences

## Alternative Approaches

1. **New Array:** Create a new array with non-target elements (violates in-place requirement)
2. **List Methods:** Use remove() method (inefficient due to shifting)
3. **Filter:** Use filter functions (violates in-place requirement)

## Common Pitfalls

1. **Extra Space:** Using additional data structures when in-place modification is required.
2. **Wrong Pointer Logic:** Not understanding when to move the slow pointer.
3. **Inefficient Methods:** Using methods that shift elements or create new arrays.
4. **Return Value:** Not understanding what the return value represents.
5. **Order Preservation:** Not maintaining the relative order of non-target elements.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/27.remove-element.py)](../exercises/27.remove-element.py)

*Note: This is a fundamental two-pointer problem that demonstrates efficient in-place element removal.*
