import java.io.*;

public class HaikuTemplate {
    /**
     * Construct and output a haiku
     * 
     * N: the number of words
     * S: the list of syllables for each word
     * W: the words themselves
     */
    static void solve(int N, int[] S, String[] W) {
        // YOUR CODE HERE
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            int[] S = new int[N];
            String[] W = new String[N];
            for (int j = 0; j < N; j++) {
                String[] SW = in.readLine().split(" ");
                S[j] = Integer.parseInt(SW[0]);
                W[j] = SW[1];
            }
            solve(N, S, W);
        }
        out.flush();
    }
}
