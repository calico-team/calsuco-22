import java.io.*;

public class BarsAlgebra {
    // Note that we change the type of N here to double
    static int solve(double N) {
        return (int) (0.5 * (Math.sqrt(8 * N + 1) - 1));
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            double N = Double.parseDouble(in.readLine());
            out.println(solve(N));
        }
        out.flush();
    }
}
