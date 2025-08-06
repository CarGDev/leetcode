# Generate Tag for Video Caption

[![Problem 3582](https://img.shields.io/badge/Problem-3582-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/generate-tag-for-video-caption/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/generate-tag-for-video-caption/)

**Problem Number:** [3582](https://leetcode.com/problems/generate-tag-for-video-caption/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** String, Regular Expression
**LeetCode Link:** [https://leetcode.com/problems/generate-tag-for-video-caption/](https://leetcode.com/problems/generate-tag-for-video-caption/)

## Problem Description

You are given a string `caption` that represents the caption of a video. You want to create a tag from the caption.

The tag should be created as follows:

1. Use the first word of the caption as the base of the tag.
2. For each subsequent word, capitalize its first letter and append it to the tag.
3. Remove all non-alphabetic characters from each word.
4. The final tag should be prefixed with `#` and limited to 100 characters.

**Example 1:**
```
Input: caption = "Hello World"
Output: "#helloWorld"
Explanation: The first word is "Hello" → "hello"
The second word is "World" → "World"
Combined: "helloWorld"
With # prefix: "#helloWorld"
```

**Example 2:**
```
Input: caption = "This is a test"
Output: "#thisIsATest"
Explanation: The first word is "This" → "this"
The second word is "is" → "Is"
The third word is "a" → "A"
The fourth word is "test" → "Test"
Combined: "thisIsATest"
With # prefix: "#thisIsATest"
```

**Example 3:**
```
Input: caption = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
Output: "#aBCDEFGHIJKLMNOPQRSTUVWXYZ"
Explanation: The tag is limited to 100 characters.
```

**Constraints:**
- `1 <= caption.length <= 1000`
- `caption` consists of English letters, digits, and spaces.

## My Approach

I used a **String Processing** approach with regular expressions to generate the tag. The key insight is to process each word individually and apply the camelCase formatting rules.

**Algorithm:**
1. Split caption into words
2. For each word:
   - Remove non-alphabetic characters using regex
   - Skip empty words
   - Convert first word to lowercase
   - Capitalize first letter of subsequent words
3. Join words together
4. Add '#' prefix and limit to 100 characters

## Solution

The solution uses string processing and regex to generate camelCase tags. See the implementation in the [solution file](../exercises/3582.generate-tag-for-video-caption.py).

**Key Points:**
- Uses regex to clean words
- Applies camelCase formatting
- Handles empty words
- Limits output to 100 characters
- Adds '#' prefix

## Time & Space Complexity

**Time Complexity:** O(n)
- Split operation: O(n)
- Regex operations: O(m) per word where m is word length
- Total: O(n)

**Space Complexity:** O(n)
- Store words array: O(n)
- Store result string: O(n)
- Total: O(n)

## Key Insights

1. **Regex Cleaning:** Use regex to remove non-alphabetic characters.

2. **CamelCase Format:** First word lowercase, others capitalized.

3. **Empty Words:** Skip words that become empty after cleaning.

4. **Character Limit:** Ensure final tag doesn't exceed 100 characters.

5. **String Processing:** Efficient string manipulation for tag generation.

6. **Edge Cases:** Handle words with only non-alphabetic characters.

## Mistakes Made

1. **Wrong Formatting:** Initially might not apply camelCase correctly.

2. **Regex Issues:** Not properly handling non-alphabetic characters.

3. **Empty Words:** Not skipping words that become empty.

4. **Character Limit:** Not enforcing 100 character limit.

## Related Problems

- **CamelCase Matching** (Problem 1023): Match camelCase patterns
- **Valid Palindrome** (Problem 125): Check if string is palindrome
- **Reverse Words in String** (Problem 151): Reverse word order
- **Valid Parentheses** (Problem 20): Validate parentheses

## Alternative Approaches

1. **Manual Processing:** Process characters manually - O(n) time
2. **Two Pass:** First clean, then format - O(n) time
3. **Built-in Functions:** Use string methods - O(n) time

## Common Pitfalls

1. **Wrong Formatting:** Not applying camelCase correctly.
2. **Regex Issues:** Not properly handling non-alphabetic characters.
3. **Empty Words:** Not skipping words that become empty.
4. **Character Limit:** Not enforcing 100 character limit.
5. **Edge Cases:** Not handling special characters properly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/3582.generate-tag-for-video-caption.py)](../exercises/3582.generate-tag-for-video-caption.py)

*Note: This is a string processing problem that demonstrates regex usage and camelCase formatting.*
