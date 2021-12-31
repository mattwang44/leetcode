/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let memo = {};
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (memo[num] !== undefined) {
            return [memo[num], i];
        }
        memo[target - num] = i;
    }
};