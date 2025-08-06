# Product of Array Except Self

[![Problem 238](https://img.shields.io/badge/Problem-238-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/product-of-array-except-self/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/product-of-array-except-self/)

**Problem Number:** [238](https://leetcode.com/problems/product-of-array-except-self/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Prefix Sum
**LeetCode Link:** [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)

## Problem Description

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: answer[0] = 3*4*2 = 24, answer[1] = 1*3*4 = 12, answer[2] = 1*2*4 = 8, answer[3] = 1*2*3 = 6
```

**Example 2:**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Explanation: answer[0] = 1*0*(-3)*3 = 0, answer[1] = (-1)*0*(-3)*3 = 0, answer[2] = (-1)*1*(-3)*3 = 9, answer[3] = (-1)*1*0*3 = 0, answer[4] = (-1)*1*0*(-3) = 0
```

**Constraints:**
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## My Approach

I used a **Two-Pass** approach to calculate the product without using division. The key insight is to use two passes: first to calculate left products, then to multiply with right products.

**Algorithm:**
1. Initialize result array with 1s
2. First pass (left to right): Calculate left products
   - For each index i, store product of all elements to the left
3. Second pass (right to left): Multiply with right products
   - For each index i, multiply with product of all elements to the right
4. Return the result array

## Solution

The solution uses two-pass approach to calculate products without division. See the implementation in the [solution file](../exercises/238.product-of-array-except-self.py).

**Key Points:**
- Uses two passes through the array
- First pass calculates left products
- Second pass multiplies with right products
- Avoids division operation
- O(n) time complexity

## Time & Space Complexity

**Time Complexity:** O(n)
- Two passes through the array
- Each pass performs constant time operations
- Total: O(n)

**Space Complexity:** O(1) (excluding output array)
- Uses only a constant amount of extra space
- Output array doesn't count for space complexity

## Key Insights

1. **Two-Pass Approach:** Using two passes avoids the need for division.

2. **Left and Right Products:** Each element's product is left_product × right_product.

3. **In-place Calculation:** Can calculate products in-place using the result array.

4. **No Division:** The approach works without using division operation.

5. **Linear Time:** Achieves O(n) time complexity with two passes.

6. **Constant Space:** Uses only O(1) extra space (excluding output).

## Mistakes Made

1. **Division Approach:** Initially might try to use division, which is not allowed.

2. **Brute Force:** Using nested loops to calculate each product.

3. **Complex Logic:** Overcomplicating the two-pass approach.

4. **Wrong Order:** Not understanding the order of the two passes.

## Related Problems

- **Trapping Rain Water** (Problem 42): Two-pass approach for water trapping
- **Candy** (Problem 135): Two-pass approach for candy distribution
- **Gas Station** (Problem 134): Circular array with two-pass logic
- **Container With Most Water** (Problem 11): Two-pointer approach

## Alternative Approaches

1. **Prefix and Suffix Arrays:** Use separate arrays for left and right products - O(n) time, O(n) space
2. **Single Pass with Division:** Use division (if allowed) - O(n) time, O(1) space
3. **Recursive:** Use recursion to calculate products - O(n) time, O(n) space

## Common Pitfalls

1. **Division Usage:** Using division when it's not allowed.
2. **Brute Force:** Using nested loops for O(n²) complexity.
3. **Complex Logic:** Overcomplicating the two-pass approach.
4. **Wrong Order:** Not understanding the order of passes.
5. **Space Inefficiency:** Using O(n) extra space when O(1) is possible.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/238.product-of-array-except-self.py)](../exercises/238.product-of-array-except-self.py)

*Note: This is a two-pass problem that demonstrates efficient product calculation without division.*
