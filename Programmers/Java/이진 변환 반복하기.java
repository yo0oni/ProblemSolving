import java.util.*;

class Solution {
    public int[] solution(String string) {
        int[] answer = {0, 0};
        int convert_count = 0;
        int zero_count = 0;
        
        while(string.length() > 1) {
            convert_count += 1;
            zero_count += string.chars().filter(c -> c == '0').count();
            
            string = string.replaceAll("0", "");
            string = Integer.toBinaryString(string.length());
            System.out.println(string.length());
            
        }
        answer[0] = convert_count;
        answer[1] = zero_count;
        
        return answer;
    }
}