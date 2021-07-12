

int searchInsert(int* nums, int numsSize, int target){
    for(int i = 0; i < numsSize; i++){
        if(nums[i] == target){
            return i;
        }
    }
    
    if(nums[0] > target){
        return 0;
    }
    if(numsSize == 1){
        return 1;
    }
    
    for(int i = 0; i < numsSize - 1; i++){
        int curr = nums[i];
        int next = nums [i + 1];
        
        if(curr < target && next > target){
            return i + 1;
        }
        
        if(i == numsSize - 2){
            return numsSize;
        }
    }
    return -1;
}