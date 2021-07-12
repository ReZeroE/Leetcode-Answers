class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> m = new HashMap<Character, Character>(){{
            put(')', '(');
            put('}', '{');
            put(']', '[');
        }};
        
        Stack<Character> stack = new Stack<Character>();
        
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(m.containsValue(c)){
                stack.push(c);
            }
            else if(m.containsKey(c)){
                if(stack.isEmpty() || m.get(c) != stack.pop()){
                    return false;
                }
            }
        }
        return stack.size() == 0;
    }
}