class Solution {
    public int removeElement(int[] nums, int val) {
        ArrayList<Integer> newNums = new ArrayList<Integer>(); 
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){
                newNums.add(nums[i]);
            }
        }
        
        for(int i = 0; i < newNums.size(); i++){
            nums[i] = newNums.get(i);
        }
        return newNums.size();
    }
}
