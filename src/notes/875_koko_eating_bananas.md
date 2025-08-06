# Koko Eating Bananas

[![Problem 875](https://img.shields.io/badge/Problem-875-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/koko-eating-bananas/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/koko-eating-bananas/)

**Problem Number:** [875](https://leetcode.com/problems/koko-eating-bananas/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Binary Search
**LeetCode Link:** [https://leetcode.com/problems/koko-eating-bananas/](https://leetcode.com/problems/koko-eating-bananas/)

## Problem Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i^th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards come back.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

**Example 1:**
```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

**Example 2:**
```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

**Example 3:**
```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

**Constraints:**
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## My Approach

I used a **Binary Search** approach to find the minimum eating speed. The key insight is to search for the minimum speed that allows Koko to finish all bananas within h hours.

**Algorithm:**
1. Define binary search range: [1, max(piles)]
2. For each mid value, calculate total hours needed
3. If hours <= h, search lower half (try smaller speed)
4. If hours > h, search upper half (need larger speed)
5. Return minimum valid speed found

## Solution

The solution uses binary search to efficiently find minimum eating speed. See the implementation in the [solution file](../exercises/875.koko-eating-bananas.py).

**Key Points:**
- Uses binary search on eating speed
- Calculates hours needed for each speed
- Tracks minimum valid speed
- Handles edge cases properly

## Time & Space Complexity

**Time Complexity:** O(n log M)
- Binary search: O(log M) where M is max(piles)
- For each search: O(n) to calculate hours
- Total: O(n log M)

**Space Complexity:** O(1)
- Uses only constant extra space
- No additional data structures needed

## Key Insights

1. **Binary Search:** Search space is eating speed, not array indices.

2. **Monotonic Function:** Higher speed means fewer hours needed.

3. **Ceiling Division:** Use (pile + speed - 1) // speed for ceiling division.

4. **Search Range:** Speed range is [1, max(piles)].

5. **Minimum Speed:** Find minimum speed that satisfies time constraint.

6. **Efficient Calculation:** Calculate total hours for given speed.

## Mistakes Made

1. **Wrong Search Space:** Initially might search wrong range.

2. **Complex Logic:** Overcomplicating the hours calculation.

3. **Wrong Division:** Not using ceiling division for pile calculation.

4. **Inefficient Approach:** Using linear search instead of binary search.

## Related Problems

- **Capacity To Ship Packages** (Problem 1011): Similar binary search problem
- **Split Array Largest Sum** (Problem 410): Binary search on sum
- **Minimum Size Subarray Sum** (Problem 209): Find minimum subarray
- **Search Insert Position** (Problem 35): Binary search variant

## Alternative Approaches

1. **Linear Search:** Try each speed from 1 to max - O(nM) time
2. **Mathematical:** Use mathematical properties to optimize - O(n log M) time
3. **Greedy:** Use greedy approach with binary search - O(n log M) time

## Common Pitfalls

1. **Wrong Search Space:** Searching wrong range for eating speed.
2. **Complex Logic:** Overcomplicating the hours calculation.
3. **Wrong Division:** Not using ceiling division for pile calculation.
4. **Inefficient Approach:** Using linear search instead of binary search.
5. **Edge Cases:** Not handling edge cases properly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/875.koko-eating-bananas.py)](../exercises/875.koko-eating-bananas.py)

*Note: This is a binary search problem that demonstrates efficient optimization search on eating speed.*
