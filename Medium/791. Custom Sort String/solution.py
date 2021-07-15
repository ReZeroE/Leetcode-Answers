class Solution:
    def customSortString(self, order: str, str: str) -> str:
        order_set = set()
        final = ''
        
        for i in order:
            for j in str:
                if i == j:
                    final += i
                order_set.add(i)
            
        for i in str:
            if i not in order_set:
                final += i
                
        return final