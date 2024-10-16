class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(char c:s.toCharArray()){
            if(c == '(' || c == '{' || c=='['){
                stack.push(c);
            }
            else if(c == ')' || c == '}' || c ==']'){
                if(stack.isEmpty()){
                    return false;
                }
                char top = stack.pop();
                if(!isMatching(top,c)){
                    return false;
                }
                    
            }
        }
        return stack.isEmpty();
        
    }
    private static boolean isMatching(char open, char close) {
        return (open == '(' && close == ')') ||
               (open == '{' && close == '}') ||
               (open == '[' && close == ']');
}}