# Roman to Integer

[![Problem 13](https://img.shields.io/badge/Problem-13-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/roman-to-integer/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/roman-to-integer/)

**Problem Number:** [13](https://leetcode.com/problems/roman-to-integer/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, Math, String
**LeetCode Link:** [https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)

## Problem Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

**Example 2:**
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.
```

**Example 3:**
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

**Constraints:**
- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`
- It is guaranteed that `s` is a valid roman numeral in the range `[1, 3999]`

## My Approach

I used a **Right-to-Left** approach with a hash table to map Roman numerals to their values. The key insight is to process the string from right to left, checking for subtraction cases when a smaller value appears before a larger one.

**Algorithm:**
1. Create a hash table mapping Roman symbols to their values
2. Process the string from right to left
3. For each character, check if it forms a subtraction case with the previous character
4. If it's a subtraction case, subtract the smaller value from the larger one
5. Otherwise, add the current character's value
6. Return the total sum

## Solution

The solution uses a right-to-left approach with hash table lookup. See the implementation in the [solution file](../exercises/13.roman-to-integer.py).

**Key Points:**
- Uses hash table for O(1) symbol-to-value lookup
- Processes string from right to left for easier subtraction handling
- Checks for all six subtraction cases explicitly
- Handles edge case for the first character

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the string once from right to left
- Hash table lookups are O(1)
- Total: O(n)

**Space Complexity:** O(1)
- Hash table has constant size (7 symbols)
- No additional space proportional to input size

## Key Insights

1. **Right-to-Left Processing:** Processing from right to left makes it easier to handle subtraction cases.

2. **Subtraction Rules:** There are exactly six cases where subtraction occurs:
   - IV (4), IX (9)
   - XL (40), XC (90)
   - CD (400), CM (900)

3. **Hash Table Efficiency:** Using a hash table provides O(1) lookup for symbol values.

4. **No Invalid Cases:** The problem guarantees valid Roman numerals, so we don't need extensive validation.

5. **Character Pairs:** Subtraction only occurs with specific character pairs, making the logic straightforward.

6. **Edge Case Handling:** The first character (rightmost) is always added, never subtracted.

## Mistakes Made

1. **Left-to-Right Processing:** Initially might process left-to-right, making subtraction logic more complex.

2. **Missing Subtraction Cases:** Forgetting to handle all six subtraction cases.

3. **Complex Logic:** Overcomplicating the subtraction detection logic.

4. **Edge Cases:** Not properly handling the first character case.

## Related Problems

- **Integer to Roman** (Problem 12): Reverse conversion from integer to Roman numeral
- **Valid Parentheses** (Problem 20): Similar pattern matching with symbols
- **Decode Ways** (Problem 91): Converting string representations to numbers
- **Basic Calculator** (Problem 224): More complex mathematical expression parsing

## Alternative Approaches

1. **Left-to-Right with Lookahead:** Process left-to-right and look ahead for subtraction cases
2. **Stack-based:** Use a stack to handle the conversion
3. **Recursive:** Use recursion to process the string

## Common Pitfalls

1. **Wrong Direction:** Processing left-to-right makes subtraction logic more complex.
2. **Missing Cases:** Not handling all six subtraction cases.
3. **Complex Logic:** Overcomplicating the subtraction detection.
4. **Edge Cases:** Not handling the first character properly.
5. **Invalid Input:** Assuming invalid Roman numerals need to be handled.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/13.roman-to-integer.py)](../exercises/13.roman-to-integer.py)

*Note: This is a straightforward string processing problem that introduces the concept of symbol-to-value mapping and special case handling.*
