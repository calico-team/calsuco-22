import java.io.*;
import java.util.Random;

public class RpsRandom {
    static char[] MOVES = {'R', 'P', 'S'};
    // Solutions should be deterministic, so we need to set our random seed
    static Random rand = new Random(1337);
    
    static char playMove() {
        return MOVES[rand.nextInt(3)];
    }
    
    static void readBotMove(char botMove) {
        // This strategy doesn't care about opponent moves, so we do nothing here
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            out.println(playMove());
            out.flush();
            readBotMove(in.readLine().charAt(0));
        }
    }
}
