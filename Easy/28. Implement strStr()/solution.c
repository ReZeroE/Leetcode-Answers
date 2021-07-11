int strStr(char * haystack, char * needle){
    if(strlen(needle) == 0) return 0;
    if(strlen(haystack) == 0) return -1;
    
    if (strlen(needle) > strlen(haystack)) return -1;
    
    int gate = 0;
    
    for(int i = 0; i <= strlen(haystack) - strlen(needle); i++){
        if(haystack[i] == needle[0]){
            for(int j = 0; j < strlen(needle); j++){
                if(haystack[i + j] == needle[j]){
                    if(j == strlen(needle) - 1){
                        gate = 1;
                    }
                }
                else break;
            }
            if(gate) return i;
        }
    }
    return -1;
}