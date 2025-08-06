# Rotate Array

[![Problem 189](https://img.shields.io/badge/Problem-189-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/rotate-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/rotate-array/)

**Problem Number:** [189](https://leetcode.com/problems/rotate-array/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Math, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/rotate-array/](https://leetcode.com/problems/rotate-array/)

## Problem Description

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

**Follow up:**
- Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

## My Approach

I used an **Auxiliary Array** approach to rotate the array. The key insight is to use a temporary array to store the rotated elements and then copy them back to the original array.

**Algorithm:**
1. Handle edge case: if array length ≤ 1, return
2. Normalize k by taking modulo with array length
3. Create auxiliary array of same size
4. Calculate new positions for each element
5. Copy elements to auxiliary array at calculated positions
6. Copy auxiliary array back to original array

## Solution

The solution uses an auxiliary array to perform the rotation. See the implementation in the [solution file](../exercises/189.rotate-array.py).

**Key Points:**
- Uses auxiliary array for rotation
- Normalizes k to handle large values
- Calculates new positions for each element
- Modifies array in-place as required
- Handles edge cases properly

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through array to calculate positions
- Copy operations: O(n)
- Total: O(n)

**Space Complexity:** O(n)
- Auxiliary array of size n
- Total: O(n)

## Key Insights

1. **Modulo Operation:** Using k % len(nums) handles cases where k > array length.

2. **Position Calculation:** Each element moves to position (i + k) % len(nums).

3. **Auxiliary Array:** Using temporary array simplifies the rotation logic.

4. **In-place Modification:** The solution modifies the original array as required.

5. **Edge Cases:** Arrays with length ≤ 1 don't need rotation.

6. **Right Rotation:** Elements move to the right by k positions.

## Mistakes Made

1. **Wrong Direction:** Initially might rotate left instead of right.

2. **Large k Values:** Not handling cases where k > array length.

3. **Complex Logic:** Overcomplicating the position calculation.

4. **Space Inefficiency:** Not using O(1) space solution when possible.

## Related Problems

- **Rotate Image** (Problem 48): Rotate 2D matrix
- **Reverse Words in a String** (Problem 151): Reverse word order
- **Reverse String** (Problem 344): Reverse character array
- **Move Zeroes** (Problem 283): Move zeros to end

## Alternative Approaches

1. **Juggling Algorithm:** Use GCD-based rotation - O(n) time, O(1) space
2. **Reversal Algorithm:** Reverse parts of array - O(n) time, O(1) space
3. **Cyclic Replacements:** Use cyclic approach - O(n) time, O(1) space

## Common Pitfalls

1. **Wrong Direction:** Rotating left instead of right.
2. **Large k Values:** Not using modulo to handle k > array length.
3. **Complex Logic:** Overcomplicating the position calculation.
4. **Space Usage:** Using O(n) space when O(1) is possible.
5. **Edge Cases:** Not handling arrays with length ≤ 1.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/189.rotate-array.py)](../exercises/189.rotate-array.py)

*Note: This is an array manipulation problem that demonstrates efficient rotation using auxiliary array.*
