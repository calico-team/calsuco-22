import java.io.*;
import java.math.BigInteger;

public class BarsArbitrary {
    // Note that we change the type of N here to String
    static String solve(String N) {
        return new BigInteger(N)
            .multiply(BigInteger.valueOf(8))
            .add(BigInteger.ONE)
            .sqrt()
            .subtract(BigInteger.ONE)
            .divide(BigInteger.TWO)
            .toString();
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String N = in.readLine();
            out.println(solve(N));
        }
        out.flush();
    }
}
