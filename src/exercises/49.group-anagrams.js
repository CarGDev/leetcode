// @leet start
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    if (strs.length < 2) return [strs];
    const map = {};
    for (const str of strs) {
        const key = str.split("").sort().join("");
        if (!map[key]) {
            map[key] = [];
        }
        map[key].push(str);
    }
    return Object.values(map);
};
// @leet end
