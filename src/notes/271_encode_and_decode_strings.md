# Encode and Decode Strings

[![Problem 271](https://img.shields.io/badge/Problem-271-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/encode-and-decode-strings/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/encode-and-decode-strings/)

**Problem Number:** [271](https://leetcode.com/problems/encode-and-decode-strings/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** String, Design
**LeetCode Link:** [https://leetcode.com/problems/encode-and-decode-strings/](https://leetcode.com/problems/encode-and-decode-strings/)

## Problem Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
```
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```

Machine 2 (receiver) has the function:
```
vector<string> decode(string s) {
  //... your code
  return strs;
}
```

So Machine 1 does:
```
string encoded_string = encode(strs);
```

and Machine 2 does:
```
vector<string> strs2 = decode(encoded_string);
```

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

You are not allowed to solve the problem using any serialize methods (such as `eval`).

**Example 1:**
```
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

**Example 2:**
```
Input: dummy_input = [""]
Output: [""]
```

**Constraints:**
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` contains any possible characters out of 256 valid ASCII characters.

**Follow up:** Could you write a generalized algorithm to work on any possible set of characters?

## My Approach

I used a **Delimiter-based** approach to encode and decode strings. The key insight is to use a special delimiter that doesn't appear in the input strings to separate them.

**Algorithm:**
1. **Encode:** Join all strings with a special delimiter
2. **Decode:** Split the encoded string by the delimiter
3. Handle edge cases (empty array, empty strings)
4. Use a complex delimiter to avoid conflicts

## Solution

The solution uses delimiter-based encoding and decoding. See the implementation in the [solution file](../exercises/271.encode-and-decode-strings.js).

**Key Points:**
- Uses special delimiter to separate strings
- Handles empty arrays and empty strings
- Simple join/split approach
- Complex delimiter to avoid conflicts

## Time & Space Complexity

**Encode Time:** O(n)
- Join operation: O(n) where n is total length of all strings

**Decode Time:** O(n)
- Split operation: O(n) where n is length of encoded string

**Space Complexity:** O(n)
- Encoded string: O(n)
- Decoded array: O(n)

## Key Insights

1. **Delimiter Choice:** Using a complex delimiter avoids conflicts with input strings.

2. **Join/Split:** Simple join and split operations are efficient.

3. **Edge Cases:** Handle empty arrays and empty strings properly.

4. **Delimiter Safety:** Complex delimiter reduces chance of appearing in input.

5. **Bidirectional:** Encode and decode must be inverse operations.

6. **Character Set:** Works with any ASCII characters.

## Mistakes Made

1. **Simple Delimiter:** Initially might use simple delimiter that conflicts with input.

2. **Edge Cases:** Not handling empty arrays or empty strings properly.

3. **Complex Logic:** Overcomplicating the encoding/decoding process.

4. **Delimiter Conflicts:** Using delimiter that might appear in input strings.

## Related Problems

- **Serialize and Deserialize Binary Tree** (Problem 297): Serialize tree structure
- **Serialize and Deserialize BST** (Problem 449): Serialize BST
- **Design HashMap** (Problem 706): Design data structure
- **Design HashSet** (Problem 705): Design data structure

## Alternative Approaches

1. **Length Prefix:** Use length prefix for each string - O(n) time
2. **Escape Characters:** Use escape characters for special cases - O(n) time
3. **Base64 Encoding:** Use base64 encoding - O(n) time

## Common Pitfalls

1. **Simple Delimiter:** Using simple delimiter that conflicts with input.
2. **Edge Cases:** Not handling empty arrays or empty strings.
3. **Complex Logic:** Overcomplicating the encoding/decoding process.
4. **Delimiter Conflicts:** Using delimiter that might appear in input strings.
5. **Character Set:** Not considering all possible ASCII characters.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/271.encode-and-decode-strings.js)](../exercises/271.encode-and-decode-strings.js)

*Note: This is a design problem that demonstrates efficient string encoding and decoding with delimiters.*
