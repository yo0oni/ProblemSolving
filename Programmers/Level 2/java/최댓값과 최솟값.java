import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        List<String> strings = List.of(s.split(" "));
        List<Integer> ints = strings.stream().map(string -> Integer.parseInt(string)).collect(Collectors.toList());
        
        int min = Collections.min(ints);
        int max = Collections.max(ints);
        
        return min + " " + max;
    }
}
