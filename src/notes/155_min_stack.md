# Min Stack

[![Problem 155](https://img.shields.io/badge/Problem-155-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/min-stack/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/min-stack/)

**Problem Number:** [155](https://leetcode.com/problems/min-stack/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Stack, Design
**LeetCode Link:** [https://leetcode.com/problems/min-stack/](https://leetcode.com/problems/min-stack/)

## Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## My Approach

I used a **Two Stack** approach to maintain both the main stack and a minimum stack. The key insight is to use a separate stack to track the minimum value at each state.

**Algorithm:**
1. Use two deques: one for main stack, one for minimum values
2. Push: Add value to main stack, add minimum of current min and new value to min stack
3. Pop: Remove from both stacks simultaneously
4. Top: Return top element of main stack
5. GetMin: Return top element of min stack

## Solution

The solution uses two stacks to maintain O(1) time complexity for all operations. See the implementation in the [solution file](../exercises/155.min-stack.py).

**Key Points:**
- Uses two deques for main stack and minimum tracking
- Maintains minimum value at each stack state
- All operations are O(1) time complexity
- Handles duplicate minimum values correctly
- Synchronized operations between both stacks

## Time & Space Complexity

**Time Complexity:** O(1) for all operations
- Push: O(1) - append to both stacks
- Pop: O(1) - remove from both stacks
- Top: O(1) - access last element
- GetMin: O(1) - access last element of min stack

**Space Complexity:** O(n)
- Main stack: O(n)
- Min stack: O(n)
- Total: O(n)

## Key Insights

1. **Two Stack Design:** Using two stacks allows O(1) minimum retrieval.

2. **Minimum Tracking:** The min stack tracks the minimum value at each state.

3. **Synchronized Operations:** Push and pop operations affect both stacks simultaneously.

4. **Duplicate Handling:** The min stack can contain duplicate values for consecutive minimums.

5. **Constant Time:** All operations maintain O(1) time complexity.

6. **Stack Property:** The min stack naturally handles the LIFO property of the main stack.

## Mistakes Made

1. **Single Stack:** Initially might try to use a single stack with complex logic.

2. **Linear Search:** Using linear search to find minimum, leading to O(n) complexity.

3. **Complex Implementation:** Overcomplicating the minimum tracking logic.

4. **Wrong Data Structure:** Not using appropriate data structures for O(1) operations.

## Related Problems

- **Max Stack** (Problem 716): Design stack with max operation
- **Valid Parentheses** (Problem 20): Stack-based parentheses validation
- **Evaluate Reverse Polish Notation** (Problem 150): Stack-based expression evaluation
- **Implement Queue using Stacks** (Problem 232): Queue implementation with stacks

## Alternative Approaches

1. **Single Stack with Pairs:** Store (value, min) pairs in single stack - O(1) time, O(n) space
2. **Variable Tracking:** Track minimum with variable and handle updates - O(1) average time
3. **Linked List:** Use linked list with minimum tracking - O(1) time, O(n) space

## Common Pitfalls

1. **Single Stack Attempt:** Trying to use single stack with complex minimum tracking.
2. **Linear Search:** Using linear search to find minimum in O(n) time.
3. **Complex Logic:** Overcomplicating the minimum tracking implementation.
4. **Wrong Data Structure:** Not using appropriate data structures for O(1) operations.
5. **Synchronization Issues:** Not properly synchronizing operations between stacks.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/155.min-stack.py)](../exercises/155.min-stack.py)

*Note: This is a design problem that demonstrates efficient stack implementation with constant time minimum retrieval.*
