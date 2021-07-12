class Solution {
    public int searchInsert(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == target) return i;
        }
        
        if(nums[0] > target){
            return 0;
        }
        
        if(nums.length == 1){
            return 1;
        }
        
        for(int i = 0; i < nums.length - 1; i++){
            
            int curr = nums[i];
            int next = nums[i + 1];
            
            if(curr < target && next > target){
                return i + 1;
            }
            
            if(i == nums.length - 2){
                return nums.length;
            }
        }
        return -1;
    }
}