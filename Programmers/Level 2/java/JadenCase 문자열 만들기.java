import java.util.StringTokenizer;

class Solution {
    public String solution(String s) {
        s = s.toLowerCase();
        StringTokenizer st = new StringTokenizer(s, " ", true);
        StringBuilder answer = new StringBuilder();
        
        while(st.hasMoreTokens()) {
            String word = st.nextToken();
            answer.append(word.substring(0,1).toUpperCase() + word.substring(1));
        }
        
        return answer.toString();
    }
}