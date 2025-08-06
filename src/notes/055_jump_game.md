# Jump Game

[![Problem 55](https://img.shields.io/badge/Problem-55-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/jump-game/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/jump-game/)

**Problem Number:** [55](https://leetcode.com/problems/jump-game/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Greedy, Dynamic Programming
**LeetCode Link:** [https://leetcode.com/problems/jump-game/](https://leetcode.com/problems/jump-game/)

## Problem Description

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

**Example 1:**
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## My Approach

I used a **Greedy** approach with dynamic tracking of the maximum reachable position. The key insight is to track the farthest position we can reach from the current position and check if we can reach each index.

**Algorithm:**
1. Initialize a variable to track the farthest reachable position
2. Iterate through each position in the array
3. If current position is beyond the farthest reachable position, return false
4. Update the farthest reachable position as max(current_farthest, current_position + jump_length)
5. Return true if we can reach the last position

## Solution

The solution uses a greedy approach with dynamic reach tracking. See the implementation in the [solution file](../exercises/55.jump-game.py).

**Key Points:**
- Uses greedy approach to track maximum reachable position
- Checks if current position is reachable before proceeding
- Updates farthest reach dynamically based on current jump
- Returns false immediately if position is unreachable
- Efficiently determines if last index is reachable

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the array once
- Each iteration performs constant time operations
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Greedy Approach:** We always want to reach the farthest possible position at each step.

2. **Reachability Check:** If we can't reach the current position, we can't reach any position beyond it.

3. **Dynamic Tracking:** We update the maximum reachable position based on the current position and its jump length.

4. **Early Termination:** We can return false as soon as we encounter an unreachable position.

5. **Optimal Substructure:** The solution for the entire array depends on the solution for subarrays.

6. **No Backtracking:** Once we determine a position is unreachable, we don't need to check further.

## Mistakes Made

1. **Backtracking Approach:** Initially might use backtracking or DFS, which is inefficient.

2. **Wrong Reach Calculation:** Not properly updating the maximum reachable position.

3. **Complex Logic:** Overcomplicating the solution with unnecessary data structures.

4. **Missing Early Termination:** Not returning false when encountering unreachable positions.

## Related Problems

- **Jump Game II** (Problem 45): Find minimum jumps to reach the end
- **Gas Station** (Problem 134): Find starting gas station for circular tour
- **Candy** (Problem 135): Distribute candies based on ratings
- **Best Time to Buy and Sell Stock** (Problem 121): Find maximum profit from stock prices

## Alternative Approaches

1. **Dynamic Programming:** Use DP array to track reachability - O(n²) time, O(n) space
2. **Backtracking:** Try all possible jumps recursively - O(2^n) time complexity
3. **BFS:** Use breadth-first search to find path - O(n²) time complexity

## Common Pitfalls

1. **Wrong Algorithm:** Using backtracking or DFS instead of greedy approach.
2. **Incorrect Reach Calculation:** Not properly updating the maximum reachable position.
3. **Missing Early Termination:** Not stopping when encountering unreachable positions.
4. **Complex Implementation:** Using unnecessary data structures or complex logic.
5. **Edge Cases:** Not handling arrays with single elements or zero jumps.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/55.jump-game.py)](../exercises/55.jump-game.py)

*Note: This is a classic greedy problem that demonstrates efficient reachability checking with dynamic position tracking.*
