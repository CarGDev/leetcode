# Add Two Numbers

[![Problem 2](https://img.shields.io/badge/Problem-2-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/add-two-numbers/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/add-two-numbers/)

**Problem Number:** [2](https://leetcode.com/problems/add-two-numbers/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Linked List, Math, Recursion
**LeetCode Link:** [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

**Constraints:**
- The number of nodes in each linked list is in the range [1, 100]
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros

## My Approach

I used an **iterative approach** to simulate the manual addition process we learned in elementary school. The key insight is to process both linked lists digit by digit, maintaining a carry value, and building the result linked list as we go.

**Algorithm:**
1. Initialize a carry variable to 0
2. Create a dummy head node for the result linked list
3. Iterate through both linked lists simultaneously:
   - Extract the current digit from each list (0 if list is exhausted)
   - Add the digits along with the carry
   - Calculate the new carry and the digit to store
   - Create a new node with the calculated digit
   - Append it to the result list
4. If there's still a carry after processing all digits, create a final node
5. Return the head of the result linked list

## Solution

The solution uses an iterative approach to add two numbers represented as linked lists. See the implementation in the [solution file](../exercises/2.add-two-numbers.py).

**Key Points:**
- Processes both lists simultaneously, handling different lengths
- Maintains a carry value throughout the addition process
- Builds the result linked list incrementally
- Handles the final carry if it exists
- Returns the result in reverse order (least significant digit first)

## Time & Space Complexity

**Time Complexity:** O(max(M, N))
- We iterate through both linked lists once
- M and N are the lengths of the input linked lists
- Each iteration performs constant time operations

**Space Complexity:** O(max(M, N))
- We create a new linked list to store the result
- The result can be at most max(M, N) + 1 digits long (due to carry)
- We use a constant amount of extra space for variables

## Key Insights

1. **Reverse Order Advantage:** The fact that digits are stored in reverse order makes the addition process straightforward - we can process from left to right, just like manual addition.

2. **Carry Management:** The carry must be tracked and added to the next position, similar to how we learned addition in school.

3. **Different Lengths:** The solution handles cases where the input lists have different lengths by treating missing digits as 0.

4. **Final Carry:** After processing all digits, if there's still a carry, it becomes the most significant digit in the result.

5. **Linked List Construction:** Building the result linked list incrementally is more efficient than converting to integers and back.

6. **No Leading Zeros:** The problem guarantees no leading zeros in input, but we need to handle the case where the result might have a leading zero (like 0 + 0 = 0).

## Mistakes Made

1. **Carry Calculation:** The initial approach of converting the sum to a string to extract carry and digit is inefficient. A more efficient approach would be to use integer division and modulo operations.

2. **Variable Naming:** The variable names could be more descriptive to improve code readability.

3. **Edge Case Handling:** Need to ensure proper handling when one list is longer than the other.

## Related Problems

- **Add Two Numbers II** (Problem 445): Similar problem but digits are stored in forward order
- **Multiply Strings** (Problem 43): Multiplying two numbers represented as strings
- **Plus One** (Problem 66): Adding one to a number represented as an array
- **Add Binary** (Problem 67): Adding two binary strings
- **Add Strings** (Problem 415): Adding two numbers represented as strings

## Alternative Approaches

1. **Recursive Solution:** Can be solved recursively by processing one digit at a time
2. **Convert to Integer:** Convert linked lists to integers, add them, then convert back (not recommended due to potential overflow)
3. **Stack-based:** Use stacks to reverse the order and then add (useful for forward order problems)

## Common Pitfalls

1. **Forgetting Final Carry:** Always check if there's a carry after processing all digits
2. **Null Pointer Exceptions:** Ensure proper null checks when accessing list nodes
3. **Memory Management:** Be careful not to lose references when building the result list
4. **Overflow:** While the problem constraints prevent integer overflow, it's good practice to consider it

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/2.add-two-numbers.py)](../exercises/2.add-two-numbers.py)

*Note: This is a fundamental linked list problem that teaches the importance of careful iteration and carry management in mathematical operations.*
