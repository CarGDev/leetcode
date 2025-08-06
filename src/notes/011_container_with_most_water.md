# Container With Most Water

[![Problem 11](https://img.shields.io/badge/Problem-11-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/container-with-most-water/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/container-with-most-water/)

**Problem Number:** [11](https://leetcode.com/problems/container-with-most-water/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Two Pointers, Greedy
**LeetCode Link:** [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

## Problem Description

Given `n` non-negative integers `height` where each represents a point at coordinate `(i, height[i])`, find two lines that together with the x-axis form a container that would hold the maximum amount of water.

Return the maximum amount of water a container can store.

**Example 1:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is obtained by choosing height[1] = 8 and height[8] = 7.
```

**Example 2:**
```
Input: height = [1,1]
Output: 1
```

**Constraints:**
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## My Approach

I used a **Two Pointer** approach starting from the widest possible container and moving inward. The key insight is that we can eliminate certain combinations by moving the pointer with the smaller height, as the width will only decrease.

**Algorithm:**
1. Initialize two pointers at the beginning and end of the array
2. Calculate the area of the current container
3. Move the pointer with the smaller height inward
4. Update the maximum area if the current area is larger
5. Continue until the pointers meet

## Solution

The solution uses a two-pointer approach to find the optimal container. See the implementation in the [solution file](../exercises/11.container-with-most-water.py).

**Key Points:**
- Uses two pointers starting from the widest possible container
- Moves the pointer with smaller height to potentially find larger areas
- Calculates area as min(height[i], height[j]) * (j - i)
- Tracks maximum area throughout the process

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the array once with two pointers
- Each iteration performs constant time operations
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Two Pointer Technique:** Starting from the widest container allows us to eliminate many combinations efficiently.

2. **Greedy Movement:** Moving the pointer with the smaller height is optimal because:
   - The width will only decrease
   - We need a taller line to potentially get a larger area
   - The current smaller line cannot be part of a larger area

3. **Area Calculation:** Area = min(height[left], height[right]) × width

4. **Optimal Substructure:** The optimal solution can be found by considering the widest container first.

5. **No Need to Check All Pairs:** The two-pointer approach eliminates the need to check all O(n²) combinations.

6. **Width Decreases:** As we move inward, the width always decreases, so we need taller lines to compensate.

## Mistakes Made

1. **Brute Force Approach:** Initially might consider checking all possible pairs, leading to O(n²) complexity.

2. **Wrong Pointer Movement:** Moving the wrong pointer can lead to missing the optimal solution.

3. **Area Calculation:** Incorrectly calculating the area or using the wrong height.

4. **Edge Cases:** Not properly handling cases with only two elements or all same heights.

## Related Problems

- **Trapping Rain Water** (Problem 42): Similar concept but with different constraints
- **Two Sum II - Input Array Is Sorted** (Problem 167): Two pointer technique in sorted array
- **3Sum** (Problem 15): Three pointer technique
- **Valid Triangle Number** (Problem 611): Using two pointers for triangle validation

## Alternative Approaches

1. **Brute Force:** Check all possible pairs - O(n²) time complexity
2. **Divide and Conquer:** Split array and find maximum in each half - O(n log n) time complexity
3. **Stack-based:** Use monotonic stack to find next greater elements

## Common Pitfalls

1. **Wrong Pointer Movement:** Moving the pointer with larger height instead of smaller height.
2. **Brute Force:** Checking all combinations instead of using the two-pointer optimization.
3. **Area Calculation:** Using max instead of min for height calculation.
4. **Edge Cases:** Not handling arrays with only two elements or all same values.
5. **Width Calculation:** Incorrectly calculating the width between pointers.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/11.container-with-most-water.py)](../exercises/11.container-with-most-water.py)

*Note: This is a classic two-pointer problem that demonstrates the greedy approach of eliminating suboptimal choices early.*
