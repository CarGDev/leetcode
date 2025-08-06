# Best Time to Buy and Sell Stock

[![Problem 121](https://img.shields.io/badge/Problem-121-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Problem Number:** [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Dynamic Programming, Greedy
**LeetCode Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Constraints:**
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## My Approach

I used a **Greedy** approach with single pass tracking. The key insight is to keep track of the minimum price seen so far and calculate the potential profit at each day.

**Algorithm:**
1. Initialize minimum price to infinity and maximum profit to 0
2. Iterate through each price in the array
3. Update minimum price if current price is lower
4. Calculate potential profit: current price - minimum price
5. Update maximum profit if current profit is higher
6. Return maximum profit found

## Solution

The solution uses a greedy approach with single pass tracking. See the implementation in the [solution file](../exercises/121.best-time-to-buy-and-sell-stock.py).

**Key Points:**
- Tracks minimum price seen so far
- Calculates potential profit at each day
- Updates maximum profit when better opportunity found
- Single pass through the array
- Handles case where no profit is possible

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through the array
- Each iteration performs constant time operations
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Greedy Approach:** We can find the maximum profit by tracking the minimum price and calculating potential profits.

2. **Single Pass:** We only need to traverse the array once, keeping track of the minimum price seen so far.

3. **Buy Before Sell:** The constraint that we must buy before selling is naturally handled by tracking minimum price.

4. **No Profit Case:** If prices are monotonically decreasing, the maximum profit will be 0.

5. **Optimal Substructure:** The solution for the entire array depends on the minimum price seen so far.

6. **Efficient Tracking:** We don't need to store all prices, just the minimum and maximum profit.

## Mistakes Made

1. **Brute Force:** Initially might try all possible buy-sell pairs, leading to O(n²) complexity.

2. **Wrong Order:** Not understanding that we must buy before selling.

3. **Complex Logic:** Overcomplicating the solution with unnecessary data structures.

4. **Missing Edge Cases:** Not handling cases where no profit is possible.

## Related Problems

- **Best Time to Buy and Sell Stock II** (Problem 122): Multiple transactions allowed
- **Best Time to Buy and Sell Stock III** (Problem 123): At most two transactions
- **Best Time to Buy and Sell Stock IV** (Problem 188): At most k transactions
- **Best Time to Buy and Sell Stock with Cooldown** (Problem 309): With cooldown period

## Alternative Approaches

1. **Dynamic Programming:** Use DP array to track maximum profit - O(n) time, O(n) space
2. **Two Pointers:** Use two pointers to track buy and sell days - O(n) time
3. **Kadane's Algorithm:** Adapt Kadane's algorithm for this problem - O(n) time

## Common Pitfalls

1. **Brute Force:** Checking all possible buy-sell pairs instead of using greedy approach.
2. **Wrong Order:** Not understanding the buy-before-sell constraint.
3. **Complex Implementation:** Using unnecessary data structures or complex logic.
4. **Edge Cases:** Not handling cases where no profit is possible.
5. **Inefficient Tracking:** Not using single pass approach.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/121.best-time-to-buy-and-sell-stock.py)](../exercises/121.best-time-to-buy-and-sell-stock.py)

*Note: This is a classic greedy problem that demonstrates efficient single-pass profit maximization.*
