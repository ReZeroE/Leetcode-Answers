int removeElement(int* nums, int numsSize, int val){
    int* newNums = calloc(numsSize, sizeof(int));
    
    int newArrCount = 0;
    for(int i = 0; i < numsSize; i++){
        int n = nums[i];
        if(n != val){
            newNums[newArrCount] = n;
            newArrCount++;
        }
    }
    
    for(int i = 0; i < numsSize; i++){
        nums[i] = newNums[i];
    }
    
    return newArrCount;
}