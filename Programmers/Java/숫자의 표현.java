class Solution {
    public int solution(int n) {
        int count = 1;
        int start = 1;
        int end = 1;
        int sum = 1;
        
        while (start <= n/2) {
            if (sum < n) {
                end += 1;
                sum += end;
            } else if (sum > n) {
                sum -= start;
                start += 1;
            } else if (sum == n) {
                count += 1;
                sum -= start;
                start += 1;
            }
        }
        return count;
    }
}