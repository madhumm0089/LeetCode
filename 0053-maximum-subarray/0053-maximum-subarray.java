class Solution {
    public int maxSubArray(int[] nums) {
        int max_sum = nums[0];
        int cur_sum = nums[0];

        for(int i = 1; i < nums.length; i++){
            if(cur_sum < 0)
                cur_sum = nums[i];

            else
                cur_sum += nums[i];

            max_sum = Math.max(max_sum, cur_sum);
        }
        return max_sum;
        
    }
}