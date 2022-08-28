import java.io.*;

public class BarsSimulation {
    static int solve(int N) {
        int day = 0, bars = N;
        while (bars - day - 1 >= 0) {
            day++;
            bars -= day;
        }
        return day;
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
