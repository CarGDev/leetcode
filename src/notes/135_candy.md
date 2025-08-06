# Candy

[![Problem 135](https://img.shields.io/badge/Problem-135-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/candy/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=HARD)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/candy/)

**Problem Number:** [135](https://leetcode.com/problems/candy/)
**Difficulty:** [Hard](https://leetcode.com/problemset/?difficulty=HARD)
**Category:** Array, Greedy
**LeetCode Link:** [https://leetcode.com/problems/candy/](https://leetcode.com/problems/candy/)

## Problem Description

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

**Example 1:**
```
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

**Example 2:**
```
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
```

**Constraints:**
- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

## My Approach

I used a **Two-Pass Greedy** approach to satisfy both left and right neighbor constraints. The key insight is to make two passes through the array: first from left to right to handle increasing ratings, then from right to left to handle decreasing ratings.

**Algorithm:**
1. Initialize all children with 1 candy
2. First pass (left to right): If current rating > previous rating, give one more candy than previous
3. Second pass (right to left): If current rating > next rating, take maximum of current candy and next candy + 1
4. Sum all candies and return the total

## Solution

The solution uses a two-pass greedy approach to satisfy neighbor constraints. See the implementation in the [solution file](../exercises/135.candy.py).

**Key Points:**
- Initializes all children with minimum 1 candy
- First pass handles increasing ratings from left to right
- Second pass handles decreasing ratings from right to left
- Uses maximum function to satisfy both constraints
- Returns sum of all distributed candies

## Time & Space Complexity

**Time Complexity:** O(n)
- Two passes through the array
- Each pass performs constant time operations
- Total: O(n)

**Space Complexity:** O(n)
- Creates an array to store candy counts
- Array size equals number of children
- Total: O(n)

## Key Insights

1. **Two-Pass Strategy:** We need two passes to handle both left and right neighbor constraints.

2. **Greedy Approach:** At each step, we give the minimum candies needed to satisfy the current constraint.

3. **Maximum Function:** When handling decreasing ratings, we take the maximum to satisfy both constraints.

4. **Minimum Initialization:** Every child must get at least 1 candy, so we start with 1 candy each.

5. **Constraint Satisfaction:** The two passes ensure that both left and right neighbor constraints are satisfied.

6. **Optimal Substructure:** The solution for each child depends only on its immediate neighbors.

## Mistakes Made

1. **Single Pass:** Initially might try to handle both constraints in a single pass.

2. **Wrong Order:** Not understanding the importance of the two-pass order.

3. **Complex Logic:** Overcomplicating the constraint satisfaction logic.

4. **Wrong Initialization:** Not starting with 1 candy for each child.

## Related Problems

- **Trapping Rain Water** (Problem 42): Two-pass approach for water trapping
- **Product of Array Except Self** (Problem 238): Two-pass approach for product calculation
- **Gas Station** (Problem 134): Greedy approach with circular array
- **Jump Game** (Problem 55): Greedy approach for reachability

## Alternative Approaches

1. **Single Pass with Stack:** Use stack to handle both directions - O(n) time, O(n) space
2. **Peak Detection:** Find peaks and valleys to calculate candies - O(n) time
3. **Dynamic Programming:** Use DP to track minimum candies needed - O(n) time, O(n) space

## Common Pitfalls

1. **Single Pass Attempt:** Trying to handle both constraints in one pass.
2. **Wrong Order:** Not understanding the importance of left-to-right then right-to-left order.
3. **Complex Logic:** Overcomplicating the constraint satisfaction.
4. **Wrong Initialization:** Not starting with 1 candy for each child.
5. **Missing Maximum:** Not using maximum function when handling decreasing ratings.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/135.candy.py)](../exercises/135.candy.py)

*Note: This is a greedy problem that demonstrates efficient two-pass constraint satisfaction.*
