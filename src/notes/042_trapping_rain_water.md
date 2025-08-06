# Trapping Rain Water

[![Problem 42](https://img.shields.io/badge/Problem-42-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/trapping-rain-water/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=HARD)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/trapping-rain-water/)

**Problem Number:** [42](https://leetcode.com/problems/trapping-rain-water/)
**Difficulty:** [Hard](https://leetcode.com/problemset/?difficulty=HARD)
**Category:** Array, Two Pointers, Dynamic Programming, Stack
**LeetCode Link:** [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped.
```

**Example 2:**
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Constraints:**
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## My Approach

I used a **Two Pointer** approach with dynamic tracking of maximum heights. The key insight is to use two pointers from both ends and track the maximum heights from left and right, calculating water trapped at each position.

**Algorithm:**
1. Initialize two pointers at the beginning and end of the array
2. Track maximum heights from left (max_left) and right (max_right)
3. Move the pointer with smaller height inward
4. For each position, calculate water trapped as min(max_left, max_right) - current_height
5. Update the corresponding maximum height if current height is larger
6. Return total water trapped

## Solution

The solution uses a two-pointer approach with dynamic maximum tracking. See the implementation in the [solution file](../exercises/42.trapping-rain-water.py).

**Key Points:**
- Uses two pointers moving from opposite ends
- Tracks maximum heights from left and right dynamically
- Calculates water trapped at each position
- Moves pointer with smaller height to ensure correct calculation
- Handles edge cases efficiently

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the array once with two pointers
- Each iteration performs constant time operations
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures proportional to input size

## Key Insights

1. **Two Pointer Technique:** Using pointers from both ends allows us to track maximum heights efficiently.

2. **Dynamic Maximum Tracking:** We update the maximum heights as we move the pointers, ensuring we always have the correct bounds.

3. **Pointer Movement Strategy:** Moving the pointer with smaller height ensures we don't miss any trapped water.

4. **Water Calculation:** Water trapped at any position is min(left_max, right_max) - current_height.

5. **Greedy Approach:** The two-pointer approach is greedy and optimal for this problem.

6. **Edge Case Handling:** The algorithm naturally handles cases with no trapped water.

## Mistakes Made

1. **Wrong Pointer Movement:** Initially might move the wrong pointer, leading to incorrect calculations.

2. **Complex Approach:** Might use a more complex approach like precomputing maximum heights.

3. **Wrong Water Calculation:** Incorrectly calculating the amount of water trapped at each position.

4. **Missing Edge Cases:** Not properly handling arrays with no trapped water.

## Related Problems

- **Container With Most Water** (Problem 11): Find maximum area between two heights
- **Largest Rectangle in Histogram** (Problem 84): Find largest rectangle in histogram
- **Maximal Rectangle** (Problem 85): Find maximal rectangle in binary matrix
- **Candy** (Problem 135): Distribute candies based on ratings

## Alternative Approaches

1. **Dynamic Programming:** Precompute left and right maximum heights - O(n) time, O(n) space
2. **Stack-based:** Use monotonic stack to find trapped water - O(n) time, O(n) space
3. **Brute Force:** Check each position with nested loops - O(n²) time complexity

## Common Pitfalls

1. **Wrong Pointer Logic:** Moving the pointer with larger height instead of smaller height.
2. **Complex Implementation:** Using unnecessary data structures or complex logic.
3. **Wrong Water Calculation:** Not understanding how to calculate trapped water correctly.
4. **Edge Cases:** Not handling cases with no trapped water or single elements.
5. **Over-engineering:** Using more complex approaches when two-pointer suffices.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/42.trapping-rain-water.py)](../exercises/42.trapping-rain-water.py)

*Note: This is a classic two-pointer problem that demonstrates efficient water trapping calculation with dynamic maximum tracking.*
