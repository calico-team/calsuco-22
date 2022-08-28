import java.io.*;

public class BarsTemplate {
    /**
     * Find and return the number of days you can eat for before running out
     * 
     * N: the number of ice cream bars you have
     */
    static int solve(int N) {
        // YOUR CODE HERE
        return 0;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            out.println(solve(N));
        }
        out.flush();
    }
}
