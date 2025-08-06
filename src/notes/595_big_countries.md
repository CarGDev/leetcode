# Big Countries

[![Problem 595](https://img.shields.io/badge/Problem-595-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/big-countries/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/big-countries/)

**Problem Number:** [595](https://leetcode.com/problems/big-countries/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Database, SQL
**LeetCode Link:** [https://leetcode.com/problems/big-countries/](https://leetcode.com/problems/big-countries/)

## Problem Description

A country is **big** if:
- it has an area of at least three million (i.e., `3000000 km²`), or
- it has a population of at least twenty-five million (i.e., `25000000`).

Write a solution to find the name, population, and area of the **big countries**.

Return the result table in **any order**.

**Example:**
```
Input: 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+

Output: 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```

## My Approach

I used a **Simple SQL Query** approach with WHERE clause to filter big countries based on the given criteria. The key insight is to use OR condition to check both area and population thresholds.

**Algorithm:**
1. Select name, population, and area columns
2. Use WHERE clause with OR condition
3. Check if area >= 3000000 OR population >= 25000000
4. Return results in any order

## Solution

The solution uses a simple SQL query with WHERE clause filtering. See the implementation in the [solution file](../exercises/595.big-countries.sql).

**Key Points:**
- Uses SELECT with specific columns
- Applies WHERE clause with OR condition
- Filters based on area and population thresholds
- Returns results in any order

## Time & Space Complexity

**Time Complexity:** O(n)
- Table scan: O(n) where n is number of rows
- WHERE clause evaluation: O(n)
- Total: O(n)

**Space Complexity:** O(k)
- Result set: O(k) where k is number of matching rows
- In worst case: O(n)

## Key Insights

1. **Simple Filtering:** Use WHERE clause with OR condition for multiple criteria.

2. **Column Selection:** Only select required columns (name, population, area).

3. **Threshold Comparison:** Compare area and population against specific thresholds.

4. **OR Logic:** Use OR to include countries that meet either condition.

5. **Order Independence:** Results can be returned in any order.

6. **Efficient Query:** Simple SELECT with WHERE is optimal for this problem.

## Mistakes Made

1. **Wrong Operator:** Initially might use AND instead of OR.

2. **Extra Columns:** Might select unnecessary columns like continent or gdp.

3. **Complex Logic:** Overcomplicating the query with unnecessary joins or subqueries.

4. **Wrong Thresholds:** Not using the correct area and population thresholds.

## Related Problems

- **Classes More Than 5 Students** (Problem 596): SQL filtering with GROUP BY
- **Not Boring Movies** (Problem 620): SQL filtering with conditions
- **Duplicate Emails** (Problem 182): SQL with GROUP BY and HAVING
- **Employees Earning More Than Their Managers** (Problem 181): SQL self-join

## Alternative Approaches

1. **UNION:** Use UNION of two separate queries - O(n) time
2. **CASE Statement:** Use CASE in WHERE clause - O(n) time
3. **Subquery:** Use subquery approach - O(n) time

## Common Pitfalls

1. **Wrong Operator:** Using AND instead of OR for the conditions.
2. **Extra Columns:** Selecting unnecessary columns in the result.
3. **Complex Logic:** Overcomplicating with unnecessary joins or subqueries.
4. **Wrong Thresholds:** Not using the correct area and population thresholds.
5. **Performance:** Not considering index usage for large tables.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/595.big-countries.sql)](../exercises/595.big-countries.sql)

*Note: This is a SQL problem that demonstrates basic filtering with WHERE clause and OR conditions.* 