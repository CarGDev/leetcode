# Top K Frequent Elements

[![Problem 347](https://img.shields.io/badge/Problem-347-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/top-k-frequent-elements/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/top-k-frequent-elements/)

**Problem Number:** [347](https://leetcode.com/problems/top-k-frequent-elements/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Hash Table, Heap (Priority Queue), Sorting
**LeetCode Link:** [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem Description

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## My Approach

I used a **Hash Table with Sorting** approach to find the top k frequent elements. The key insight is to count frequencies, sort by frequency, and return the top k elements.

**Algorithm:**
1. Use hash table to count frequency of each element
2. Convert hash table to array of [element, frequency] pairs
3. Sort array by frequency in descending order
4. Extract first k elements
5. Return array of elements (not frequencies)

## Solution

The solution uses hash table and sorting to find top k frequent elements. See the implementation in the [solution file](../exercises/347.top-k-frequent-elements.js).

**Key Points:**
- Uses hash table for frequency counting
- Sorts by frequency in descending order
- Extracts top k elements
- Returns elements, not frequencies

## Time & Space Complexity

**Time Complexity:** O(n log n)
- Hash table creation: O(n)
- Sorting: O(n log n)
- Total: O(n log n)

**Space Complexity:** O(n)
- Hash table: O(n)
- Sorted array: O(n)
- Total: O(n)

## Key Insights

1. **Frequency Counting:** Using hash table provides efficient frequency counting.

2. **Sorting:** Sorting by frequency allows easy extraction of top k elements.

3. **Element Extraction:** Return elements, not their frequencies.

4. **Unique Elements:** Problem guarantees unique answer.

5. **Order Independence:** Answer can be returned in any order.

6. **Follow-up Challenge:** Can be optimized to O(n) using heap or bucket sort.

## Mistakes Made

1. **Wrong Return:** Initially might return frequencies instead of elements.

2. **Complex Logic:** Overcomplicating the frequency counting.

3. **Inefficient Approach:** Using O(n²) approach when sorting suffices.

4. **Wrong Sorting:** Not sorting by frequency in correct order.

## Related Problems

- **Sort Characters By Frequency** (Problem 451): Sort characters by frequency
- **Kth Largest Element** (Problem 215): Find kth largest element
- **Majority Element** (Problem 169): Find majority element
- **Group Anagrams** (Problem 49): Group strings by anagrams

## Alternative Approaches

1. **Heap (Priority Queue):** Use max heap for O(n log k) time
2. **Bucket Sort:** Use bucket sort for O(n) time
3. **Quick Select:** Use quick select for O(n) average time

## Common Pitfalls

1. **Wrong Return:** Returning frequencies instead of elements.
2. **Complex Logic:** Overcomplicating the frequency counting.
3. **Inefficient Approach:** Using O(n²) approach when sorting suffices.
4. **Wrong Sorting:** Not sorting by frequency in correct order.
5. **Follow-up Challenge:** Not considering O(n) solutions.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/347.top-k-frequent-elements.js)](../exercises/347.top-k-frequent-elements.js)

*Note: This is a hash table problem that demonstrates efficient frequency counting and sorting for top k elements.*
