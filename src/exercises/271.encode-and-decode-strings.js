// @leet start
/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
var key = '$#@C$(){(($[]%^[$()${#${(}'
var encode = function(strs) {
    if (strs.length === 0) return [];
    const encoded = strs.join(key);
    return encoded;
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
var decode = function(str) {
    if (Array.isArray(str)) return str;
    let decoded = str.split(key);
    return decoded;
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */
// @leet end
