// @leet start
/**
 * @param {number} n
 * @return {number}
 */
const fibonacci = (element, cache = []) => {
            if (element === 0) return 0;
            if (element === 1) return 1;
            if (cache[element]) return cache[element];
            cache[element] = fibonacci(element - 2, cache) + fibonacci(element - 1, cache);
            return cache[element];
            }
var climbStairs = function(n) {
    

            const array = fibonacci(n + 1)
            return array
};
// @leet end
