# Two Sum II - Input Array Is Sorted

[![Problem 167](https://img.shields.io/badge/Problem-167-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Problem Number:** [167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Two Pointers, Binary Search
**LeetCode Link:** [https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Problem Description

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You may not use the same element twice.

Your solution must use only constant extra space.

**Example 1:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2:**
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3:**
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

**Constraints:**
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution.

## My Approach

I used a **Two Pointers** approach to find the pair that sums to the target. The key insight is to use the sorted property of the array to efficiently narrow down the search space.

**Algorithm:**
1. Initialize two pointers: left at start, right at end
2. While left < right:
   - Calculate the sum of elements at left and right pointers
   - If sum equals target, return the 1-indexed positions
   - If sum is less than target, move left pointer right
   - If sum is greater than target, move right pointer left
3. Return the 1-indexed positions when target is found

## Solution

The solution uses two pointers to efficiently find the target sum in O(n) time. See the implementation in the [solution file](../exercises/167.two-sum-ii-input-array-is-sorted.py).

**Key Points:**
- Uses two pointers starting from opposite ends
- Leverages sorted property to eliminate search space
- Returns 1-indexed positions as required
- Constant space complexity
- Guaranteed to find solution

## Time & Space Complexity

**Time Complexity:** O(n)
- Two pointers traverse the array at most once
- Each iteration performs constant time operations
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Sorted Property:** The array is sorted, allowing efficient two-pointer approach.

2. **Two Pointers:** Using pointers from both ends eliminates the need for nested loops.

3. **Sum Comparison:** Comparing current sum with target guides pointer movement.

4. **1-Indexed Output:** Remember to add 1 to indices for the required output format.

5. **Guaranteed Solution:** The problem guarantees exactly one solution exists.

6. **Constant Space:** The approach uses only constant extra space.

## Mistakes Made

1. **Hash Table:** Initially might use hash table approach, requiring O(n) space.

2. **Binary Search:** Using binary search for each element, leading to O(n log n) complexity.

3. **Wrong Indexing:** Forgetting to add 1 to indices for 1-indexed output.

4. **Complex Logic:** Overcomplicating the two-pointer movement logic.

## Related Problems

- **Two Sum** (Problem 1): Find two numbers that sum to target
- **3Sum** (Problem 15): Find three numbers that sum to zero
- **Container With Most Water** (Problem 11): Two pointer approach for area
- **Trapping Rain Water** (Problem 42): Two pointer approach for water trapping

## Alternative Approaches

1. **Hash Table:** Use hash set to track seen numbers - O(n) time, O(n) space
2. **Binary Search:** For each element, binary search for complement - O(n log n) time
3. **Brute Force:** Check all pairs - O(n²) time, O(1) space

## Common Pitfalls

1. **Hash Table Usage:** Using hash table when two pointers are more efficient.
2. **Wrong Indexing:** Not adding 1 to indices for 1-indexed output.
3. **Complex Logic:** Overcomplicating the two-pointer movement.
4. **Space Inefficiency:** Using O(n) space when O(1) is possible.
5. **Wrong Movement:** Not understanding when to move which pointer.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/167.two-sum-ii-input-array-is-sorted.py)](../exercises/167.two-sum-ii-input-array-is-sorted.py)

*Note: This is a classic two-pointer problem that demonstrates efficient searching in sorted arrays.*
