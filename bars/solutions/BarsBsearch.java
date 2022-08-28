import java.io.*;

public class BarsBsearch {
    // Note that we need to use long long values because N can exceed the
    // maximum 32 bit integer.
    static long solve(long N) {
        // We set hi to Integer.MAX_VALUE instead of Long.MAX_VALUE to prevent
        // multiplication overflow. It can be proven that all answers for 2B
        // are smaller.
        long lo = 0, hi = Integer.MAX_VALUE, best = 0;
        while (lo <= hi) {
            long guess = (hi + lo) / 2;
            if (guess * (guess + 1) / 2 <= N) {
                best = guess;
                lo = guess + 1;
            } else {
                hi = guess - 1;
            }
        }
        return best;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            long N = Long.parseLong(in.readLine());
            out.println(solve(N));
        }
        out.flush();
    }
}
