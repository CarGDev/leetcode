# Two Sum

[![Problem 1](https://img.shields.io/badge/Problem-1-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/two-sum/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/two-sum/)

**Problem Number:** [1](https://leetcode.com/problems/two-sum/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Hash Table
**LeetCode Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## My Approach

I used a **Hash Table (Dictionary)** approach to solve this problem efficiently. The key insight is to use a hash map to store previously seen numbers and their indices, allowing us to find the complement in O(1) time.

**Algorithm:**
1. Create an empty hash map to store numbers and their indices
2. Iterate through the array once
3. For each number, calculate its complement (target - current_number)
4. Check if the complement exists in the hash map
5. If found, return the current index and the complement's index
6. If not found, add the current number and its index to the hash map

## Solution

The solution uses a hash table approach to achieve O(n) time complexity. See the implementation in the [solution file](../exercises/1.two-sum.py).

**Key Points:**
- Uses a hash map for O(1) lookup time
- Only requires a single pass through the array
- Handles edge cases appropriately
- Returns indices in the order [current_index, complement_index]

## Time & Space Complexity

**Time Complexity:** O(n)
- We iterate through the array once: O(n)
- Hash map operations (insertion and lookup) are O(1) on average
- Total: O(n)

**Space Complexity:** O(n)
- In the worst case, we might need to store all n elements in the hash map
- This occurs when the solution is found at the end of the array

## Key Insights

1. **Hash Table Efficiency:** Using a hash table allows us to achieve O(n) time complexity instead of the O(n²) that would result from a brute force approach with nested loops.

2. **Single Pass Solution:** We can find the solution in just one iteration through the array by storing previously seen numbers and checking for complements.

3. **Complement Strategy:** Instead of looking for two numbers that sum to target, we look for one number and its complement (target - number).

4. **Edge Case Handling:** The solution includes proper handling of edge cases like empty arrays and arrays with fewer than 2 elements.

5. **No Duplicate Usage:** The algorithm naturally avoids using the same element twice because we check for the complement before adding the current element to the hash map.

## Mistakes Made

1. **Initial Edge Case Over-engineering:** The solution includes edge cases for arrays with 0, 1, or 2 elements, which might be unnecessary given the problem constraints (array length ≥ 2).

2. **Return Order:** The solution returns [current_index, complement_index], but the problem allows returning the answer in any order.

## Related Problems

- **Two Sum II - Input Array Is Sorted** (Problem 167): Similar problem but with a sorted array, allowing for a two-pointer approach
- **Two Sum BST** (Problem 653): Finding two nodes in a BST that sum to target
- **Three Sum** (Problem 15): Extension to finding three numbers that sum to zero
- **Four Sum** (Problem 18): Further extension to finding four numbers that sum to target

## Alternative Approaches

1. **Brute Force:** O(n²) time complexity with nested loops
2. **Two Pointers:** Only works for sorted arrays, O(n log n) due to sorting
3. **Binary Search:** Only applicable for sorted arrays

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/1.two-sum.py)](../exercises/1.two-sum.py)

*Note: This is a fundamental problem that introduces the hash table optimization pattern, commonly used in array and string problems.*
