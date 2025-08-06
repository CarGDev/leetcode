# Max Points on a Line

[![Problem 149](https://img.shields.io/badge/Problem-149-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/max-points-on-a-line/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=HARD)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/max-points-on-a-line/)

**Problem Number:** [149](https://leetcode.com/problems/max-points-on-a-line/)
**Difficulty:** [Hard](https://leetcode.com/problemset/?difficulty=HARD)
**Category:** Array, Hash Table, Math, Geometry
**LeetCode Link:** [https://leetcode.com/problems/max-points-on-a-line/](https://leetcode.com/problems/max-points-on-a-line/)

## Problem Description

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return the maximum number of points that lie on the same straight line.

**Example 1:**
```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Explanation: All points lie on the line y = x.
```

**Example 2:**
```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation: The line through points [1,1], [4,1] contains 4 points.
```

**Constraints:**
- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= xi, yi <= 10^4`
- All the points are unique.

## My Approach

I used a **Hash Table** approach with slope calculation. The key insight is to calculate the slope between each pair of points and count how many points share the same slope from a fixed reference point.

**Algorithm:**
1. Handle edge cases (≤ 2 points return length)
2. For each point as reference, calculate slopes to all other points
3. Use hash table to count points with same slope
4. Handle vertical lines (infinite slope) separately
5. Track maximum points found on any line
6. Return maximum count + 1 (including reference point)

## Solution

The solution uses hash table with slope calculation to find maximum points on a line. See the implementation in the [solution file](../exercises/149.max-points-on-a-line.py).

**Key Points:**
- Uses hash table to count points with same slope
- Handles vertical lines (infinite slope) with special case
- Calculates slope using (y2-y1)/(x2-x1) formula
- Tracks maximum points found for each reference point
- Returns maximum count including reference point

## Time & Space Complexity

**Time Complexity:** O(n²)
- For each point, check all other points
- Slope calculation is constant time
- Total: O(n²)

**Space Complexity:** O(n)
- Hash table stores at most n-1 slopes
- Each slope can have multiple points
- Total: O(n)

## Key Insights

1. **Slope as Key:** Using slope as hash table key groups points on same line.

2. **Reference Point:** For each reference point, we calculate slopes to all other points.

3. **Vertical Lines:** Vertical lines have infinite slope and need special handling.

4. **Duplicate Points:** The problem guarantees unique points, simplifying the logic.

5. **Maximum Tracking:** We track the maximum points found for each reference point.

6. **Slope Formula:** Using (y2-y1)/(x2-x1) to calculate slope between two points.

## Mistakes Made

1. **Floating Point Precision:** Using floating point for slope comparison can lead to precision issues.

2. **Vertical Line Handling:** Not properly handling vertical lines with infinite slope.

3. **Reference Point Logic:** Not understanding that we need to check each point as reference.

4. **Complex Implementation:** Overcomplicating the slope calculation and counting.

## Related Problems

- **Line Reflection** (Problem 356): Check if points are symmetric about a line
- **Convex Hull** (Problem 587): Find convex hull of points
- **Rectangle Area** (Problem 223): Calculate area of overlapping rectangles
- **Valid Square** (Problem 593): Check if four points form a square

## Alternative Approaches

1. **GCD for Slope:** Use GCD to represent slope as reduced fraction - O(n²) time
2. **Cross Product:** Use cross product to check collinearity - O(n²) time
3. **Brute Force:** Check all possible lines through point pairs - O(n³) time

## Common Pitfalls

1. **Floating Point Issues:** Using floating point for slope comparison.
2. **Vertical Line Handling:** Not properly handling infinite slopes.
3. **Reference Point Logic:** Not checking each point as potential reference.
4. **Complex Implementation:** Overcomplicating the slope calculation.
5. **Edge Cases:** Not handling cases with ≤ 2 points properly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/149.max-points-on-a-line.py)](../exercises/149.max-points-on-a-line.py)

*Note: This is a geometry problem that demonstrates efficient slope-based line detection with hash tables.*

