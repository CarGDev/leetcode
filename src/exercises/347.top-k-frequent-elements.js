// @leet start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const setOfNumbers = {};
    for (const num of nums) {
        if (!setOfNumbers[num]) {
            setOfNumbers[num] = 1;
        } else {
            setOfNumbers[num] = setOfNumbers[num] + 1;
        }
    }
    const values = Object.values(setOfNumbers);
    const keys = Object.keys(setOfNumbers);
    let newArray = [];

    for (let i = 0; i < keys.length; i++) {
        newArray.push([keys[i], values[i]]);
    }
    newArray = newArray.sort((a, b) => {
        return b[1] - a[1];
    });
    newArray = newArray.slice(0, k);
    newArray = newArray.map((a) => Number(a[0]));
    return newArray;
};
// @leet end
