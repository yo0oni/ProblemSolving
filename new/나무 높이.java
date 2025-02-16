import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int test;
    static int[] trees;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        test = Integer.parseInt(br.readLine());

        for (int t = 1; t <= test; t++) {
            int n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            trees = new int[n];

            int maxHeight = 0;
            for (int i = 0; i < n; i++) {
                trees[i] = Integer.parseInt(st.nextToken());
                maxHeight = Math.max(maxHeight, trees[i]);
            }

            int evenCount = 0;  // 2씩 증가할 수 있는 횟수
            int oddCount = 0;  // 1씩 증가할 수 있는 횟수

            for (int i = 0; i < n; i++) {
                int diff = maxHeight - trees[i]; 
                evenCount += diff / 2;
                oddCount += diff % 2; 
            }

            // (짝수 + 홀수 증가 횟수를 적절히 조합하여 최소 일수 계산)
            while (evenCount > oddCount + 1) {
                evenCount -= 1;
                oddCount += 2;
            }

            int answer;
			if(oddCount > evenCount) {
				answer = oddCount * 2 - 1;
				
			} else if(evenCount > oddCount) {
				answer = evenCount * 2;
				
			} else {
				answer = oddCount + evenCount;
			}
			
			System.out.println("#" + t + " " + answer);
        }
    }
}