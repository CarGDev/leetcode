# Contains Duplicate II

[![Problem 219](https://img.shields.io/badge/Problem-219-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/contains-duplicate-ii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/contains-duplicate-ii/)

**Problem Number:** [219](https://leetcode.com/problems/contains-duplicate-ii/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Hash Table, Sliding Window
**LeetCode Link:** [https://leetcode.com/problems/contains-duplicate-ii/](https://leetcode.com/problems/contains-duplicate-ii/)

## Problem Description

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Example 1:**
```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**
```
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `0 <= k <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## My Approach

I used a **Sliding Window** approach with hash set to track elements within the window. The key insight is to maintain a sliding window of size k+1 and check for duplicates within this window.

**Algorithm:**
1. Handle edge case: if array length ≤ 1, return False
2. Initialize hash set to track elements in current window
3. For each element:
   - If element already in set, return True (duplicate found)
   - Add element to set
   - If set size > k, remove oldest element (nums[i-k])
4. Return False if no duplicates found

## Solution

The solution uses sliding window with hash set to check for duplicates within k distance. See the implementation in the [solution file](../exercises/219.contains-duplicate-ii.py).

**Key Points:**
- Uses sliding window of size k+1
- Maintains hash set for O(1) lookup
- Removes oldest element when window exceeds k
- Returns True as soon as duplicate is found
- Handles edge cases properly

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through the array
- Hash set operations are O(1)
- Total: O(n)

**Space Complexity:** O(k)
- Hash set stores at most k+1 elements
- Total: O(k)

## Key Insights

1. **Sliding Window:** Using sliding window of size k+1 ensures we only check elements within k distance.

2. **Hash Set:** Using hash set provides O(1) lookup for duplicates.

3. **Window Management:** Removing oldest element when window exceeds k maintains the sliding window.

4. **Early Return:** Return True as soon as duplicate is found within the window.

5. **Distance Constraint:** The k parameter limits the window size and search space.

6. **Efficient Removal:** Removing oldest element keeps the window size bounded.

## Mistakes Made

1. **Wrong Window Size:** Initially might use wrong window size.

2. **Complex Logic:** Overcomplicating the sliding window management.

3. **Wrong Removal:** Not removing the correct element when window exceeds k.

4. **Missing Edge Cases:** Not handling arrays with length ≤ 1.

## Related Problems

- **Contains Duplicate** (Problem 217): Check for any duplicates
- **Contains Duplicate III** (Problem 220): Check for duplicates within k distance and t difference
- **Longest Substring Without Repeating Characters** (Problem 3): Find longest unique substring
- **Minimum Size Subarray Sum** (Problem 209): Find minimum subarray with given sum

## Alternative Approaches

1. **Hash Map with Indices:** Store indices in hash map - O(n) time, O(n) space
2. **Brute Force:** Check all pairs within k distance - O(nk) time, O(1) space
3. **Sorting with Indices:** Sort with indices and check adjacent - O(n log n) time, O(n) space

## Common Pitfalls

1. **Wrong Window Size:** Using incorrect window size for sliding window.
2. **Complex Logic:** Overcomplicating the sliding window management.
3. **Wrong Removal:** Not removing the correct element when window exceeds k.
4. **Missing Edge Cases:** Not handling edge cases properly.
5. **Inefficient Approach:** Using brute force when sliding window is more efficient.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/219.contains-duplicate-ii.py)](../exercises/219.contains-duplicate-ii.py)

*Note: This is a sliding window problem that demonstrates efficient duplicate detection within a distance constraint.*
