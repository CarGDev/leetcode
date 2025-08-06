# Best Time to Buy and Sell Stock II

[![Problem 122](https://img.shields.io/badge/Problem-122-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

**Problem Number:** [122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Dynamic Programming, Greedy
**LeetCode Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

## Problem Description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```

**Example 2:**
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```

**Example 3:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
```

**Constraints:**
- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## My Approach

I used a **Greedy** approach that captures all positive price differences. The key insight is that we can capture all the profit by buying and selling whenever the price increases from one day to the next.

**Algorithm:**
1. Initialize total profit to 0 and buy price to first day's price
2. Iterate through prices starting from the second day
3. Calculate potential profit: current price - buy price
4. If profit is positive, add it to total profit
5. Update buy price to current price (for next potential transaction)
6. Return total accumulated profit

## Solution

The solution uses a greedy approach to capture all positive price differences. See the implementation in the [solution file](../exercises/122.best-time-to-buy-and-sell-stock-ii.py).

**Key Points:**
- Captures all positive price differences
- Buys and sells whenever price increases
- Accumulates total profit from all transactions
- Handles multiple buy-sell cycles
- Single pass through the array

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through the array
- Each iteration performs constant time operations
- Total: O(n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Greedy Strategy:** We can capture all profit by buying and selling whenever the price increases.

2. **Multiple Transactions:** Unlike the first problem, we can make multiple buy-sell transactions.

3. **Positive Differences:** We only need to capture positive price differences between consecutive days.

4. **Immediate Selling:** We can buy and sell on the same day, which simplifies the strategy.

5. **Optimal Substructure:** The total profit is the sum of all positive price differences.

6. **No Holding Cost:** Since we can hold at most one share, we don't need to track holding periods.

## Mistakes Made

1. **Complex DP:** Initially might use dynamic programming when greedy approach suffices.

2. **Wrong Strategy:** Not understanding that we can capture all positive differences.

3. **Over-engineering:** Using complex logic to track buy-sell cycles.

4. **Missing Transactions:** Not capturing all profitable opportunities.

## Related Problems

- **Best Time to Buy and Sell Stock** (Problem 121): Single transaction
- **Best Time to Buy and Sell Stock III** (Problem 123): At most two transactions
- **Best Time to Buy and Sell Stock IV** (Problem 188): At most k transactions
- **Best Time to Buy and Sell Stock with Cooldown** (Problem 309): With cooldown period

## Alternative Approaches

1. **Dynamic Programming:** Use DP to track maximum profit with state tracking - O(n) time, O(n) space
2. **Peak Valley:** Find all peaks and valleys to calculate total profit - O(n) time
3. **Cumulative Sum:** Calculate cumulative sum of positive differences - O(n) time

## Common Pitfalls

1. **Complex Implementation:** Using dynamic programming when greedy approach is simpler.
2. **Wrong Strategy:** Not capturing all positive price differences.
3. **Over-engineering:** Using complex logic to track transactions.
4. **Missing Opportunities:** Not understanding that we can make multiple transactions.
5. **Inefficient Approach:** Not using the greedy insight about positive differences.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/122.best-time-to-buy-and-sell-stock-ii.py)](../exercises/122.best-time-to-buy-and-sell-stock-ii.py)

*Note: This is a greedy problem that demonstrates capturing all positive price differences for maximum profit.*
