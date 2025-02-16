package Java.SWEA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

class SWEA1249 {
    static int[][] board;
    static int[][] time;
    static int size;
    static int[] di = new int[]{1, 0, -1, 0};
    static int[] dj = new int[]{0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        // 도로가 파여진 깊이에 비례해서 복구 시간은 증가한다.
        // 깊이 1 == 복구 시간 1
        // answer = 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간

        // 0 == 복구작업 불필요
        // 그외 == 복구작업 소요 시간
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for(int tc = 1; tc <= testCase; tc ++) {
            size = Integer.parseInt(br.readLine());
            board = new int[size][size];
            time = new int[size][size];

            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    time[i][j] = Integer.MAX_VALUE;
                }
            }
            time[0][0] = board[0][0];

            for (int i = 0; i < size; i++) {
                String[] tokens = br.readLine().split("");
                
                for(int j = 0; j < size; j ++) {
                    board[i][j] = Integer.parseInt(tokens[j]);
                }
            }
            System.out.println("#" + tc + " " + bfs(0, 0));
        }
    }

    static int bfs(int si, int sj) {
        Queue<int[]> dq = new ArrayDeque<>();
        boolean[][] visited = new boolean[size][size];
        dq.add(new int[]{si, sj, board[si][sj]});
        visited[si][sj] = true;

        while (!dq.isEmpty()) {
            int[] current = dq.poll();
            int ci = current[0];
            int cj = current[1];

            for(int d = 0; d < 4; d ++) {
                int ni = di[d] + ci;
                int nj = dj[d] + cj;

                if (validate(ni, nj) && !visited[ni][nj]) {
                    int total_time = time[ci][cj] + board[ni][nj];

                    if (total_time < time[ni][nj]) {
                        dq.add(new int[]{ni, nj});
                        time[ni][nj] = total_time;
                    }
                }
            }
        }
        return time[size-1][size-1];
    }

    static boolean validate(int i, int j) {
        return 0 <= i && i < size && 0 <= j && j < size;
    }
}