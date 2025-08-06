# Binary Search

[![Problem 704](https://img.shields.io/badge/Problem-704-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/binary-search/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/binary-search/)

**Problem Number:** [704](https://leetcode.com/problems/binary-search/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Binary Search
**LeetCode Link:** [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/)

## Problem Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**
```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## My Approach

I used a **Recursive Binary Search** approach to find the target in the sorted array. The key insight is to use divide-and-conquer strategy to reduce search space by half in each iteration.

**Algorithm:**
1. Define recursive function with low and high bounds
2. Base case: if low > high, return -1 (not found)
3. Calculate mid point
4. Check if target is at low, high, or mid
5. If target < nums[mid], search left half
6. If target > nums[mid], search right half
7. Return index if found, -1 otherwise

## Solution

The solution uses recursive binary search to efficiently find target in sorted array. See the implementation in the [solution file](../exercises/704.binary-search.py).

**Key Points:**
- Uses recursive binary search
- Checks boundary conditions first
- Reduces search space by half each iteration
- Returns index or -1 if not found

## Time & Space Complexity

**Time Complexity:** O(log n)
- Each recursive call reduces search space by half
- Total recursive calls: O(log n)

**Space Complexity:** O(log n)
- Recursive call stack depth: O(log n)
- Each call uses constant space

## Key Insights

1. **Divide and Conquer:** Binary search reduces problem size by half each iteration.

2. **Sorted Array:** Binary search requires sorted array for O(log n) complexity.

3. **Boundary Checks:** Check low and high bounds before mid for efficiency.

4. **Recursive Approach:** Recursive implementation is clean and intuitive.

5. **Early Termination:** Can terminate early if target found at boundaries.

6. **Unique Elements:** Problem guarantees unique elements in array.

## Mistakes Made

1. **Wrong Bounds:** Initially might use wrong bounds for recursive calls.

2. **Infinite Recursion:** Not handling base case properly.

3. **Complex Logic:** Overcomplicating the binary search logic.

4. **Wrong Mid Calculation:** Using wrong formula for mid calculation.

## Related Problems

- **Search Insert Position** (Problem 35): Find insertion position
- **Find First and Last Position** (Problem 34): Find range of target
- **Search in Rotated Sorted Array** (Problem 33): Search in rotated array
- **Find Minimum in Rotated Sorted Array** (Problem 153): Find minimum element

## Alternative Approaches

1. **Iterative Binary Search:** Use while loop instead of recursion - O(log n) time, O(1) space
2. **Built-in Binary Search:** Use bisect module - O(log n) time
3. **Linear Search:** Use linear search - O(n) time (not optimal)

## Common Pitfalls

1. **Wrong Bounds:** Using wrong bounds for recursive calls.
2. **Infinite Recursion:** Not handling base case properly.
3. **Complex Logic:** Overcomplicating the binary search logic.
4. **Wrong Mid Calculation:** Using wrong formula for mid calculation.
5. **Overflow:** Not handling integer overflow in mid calculation.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/704.binary-search.py)](../exercises/704.binary-search.py)

*Note: This is a binary search problem that demonstrates efficient divide-and-conquer strategy for searching in sorted arrays.*
