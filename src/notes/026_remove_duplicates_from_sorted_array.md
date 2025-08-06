# Remove Duplicates from Sorted Array

[![Problem 26](https://img.shields.io/badge/Problem-26-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Problem Number:** [26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/remove-duplicates-from-sorted-array/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
2. Return `k`.

**Example 1:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order

## My Approach

I used a **Two Pointer** approach with in-place modification. The key insight is to use a slow pointer to track the position where the next unique element should be placed, and a fast pointer to scan through the array.

**Algorithm:**
1. Handle edge case (empty array returns 0)
2. Initialize slow pointer k at index 0
3. Iterate through array with fast pointer i
4. When nums[i] != nums[k], increment k and copy nums[i] to nums[k]
5. Return k + 1 (number of unique elements)

## Solution

The solution uses a two-pointer approach for in-place duplicate removal. See the implementation in the [solution file](../exercises/26.remove-duplicates-from-sorted-array.py).

**Key Points:**
- Uses two pointers: slow pointer (k) and fast pointer (i)
- Modifies array in-place without extra space
- Maintains relative order of elements
- Returns count of unique elements
- Handles edge case of empty array

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the array once with the fast pointer
- Each element is compared and potentially copied once
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- Modifies the array in-place
- No additional data structures needed

## Key Insights

1. **Two Pointer Technique:** Using a slow pointer to track the next position for unique elements and a fast pointer to scan through the array.

2. **In-Place Modification:** The problem requires modifying the array in-place, which is efficiently done with two pointers.

3. **Sorted Array Advantage:** Since the array is sorted, duplicates are always adjacent, making the comparison simple.

4. **Relative Order Preservation:** The two-pointer approach naturally preserves the relative order of elements.

5. **Efficient Copying:** We only copy elements when we find a new unique value, minimizing unnecessary operations.

6. **Return Value:** The function returns the count of unique elements, which is k + 1 (since k is 0-indexed).

## Mistakes Made

1. **Extra Space Usage:** Initially might use a hash set or new array, which violates the in-place requirement.

2. **Wrong Pointer Logic:** Not properly understanding when to increment the slow pointer.

3. **Return Value Confusion:** Returning the wrong value (k instead of k + 1).

4. **Edge Case Handling:** Not properly handling empty arrays.

## Related Problems

- **Remove Duplicates from Sorted Array II** (Problem 80): Allow at most 2 occurrences of each element
- **Remove Element** (Problem 27): Remove all instances of a specific value
- **Move Zeroes** (Problem 283): Move all zeros to the end while maintaining order
- **Sort Colors** (Problem 75): Sort array with only 0, 1, 2 values

## Alternative Approaches

1. **Hash Set:** Use a set to track seen elements (violates in-place requirement)
2. **New Array:** Create a new array with unique elements (violates in-place requirement)
3. **Library Functions:** Use built-in functions like set() (not allowed for this problem)

## Common Pitfalls

1. **Extra Space:** Using additional data structures when in-place modification is required.
2. **Wrong Return Value:** Returning k instead of k + 1.
3. **Pointer Logic:** Not understanding when to move the slow pointer.
4. **Edge Cases:** Not handling empty arrays properly.
5. **Order Preservation:** Not maintaining the relative order of elements.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/26.remove-duplicates-from-sorted-array.py)](../exercises/26.remove-duplicates-from-sorted-array.py)

*Note: This is a fundamental two-pointer problem that demonstrates efficient in-place array modification.*
