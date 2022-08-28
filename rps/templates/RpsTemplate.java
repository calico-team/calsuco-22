import java.io.*;

public class RpsTemplate {
    /**
     * Determine what move to play this round of rock paper scissors and return it
     */
    static char playMove() {
        // YOUR CODE HERE
        return ' ';
    }
    
    /**
     * Read in the opponent's move for this round of rock paper scissors
     * 
     * botMove: the move made by the bot
     */
    static void readBotMove(String botMove) {
        // YOUR CODE HERE
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            out.println(playMove());
            out.flush();
            readBotMove(in.readLine());
        }
    }
}
