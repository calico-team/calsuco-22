import java.io.*;

public class RpsPattern {
    static int roundNum = 0;
    
    static char playMove() {
        // This is a different pattern from what was described in the solution!
        // Can you figure out why it also works?
        switch(roundNum % 3) {
            case 0:
                return 'R';
            case 1:
                return 'P';
            default:
                return 'S';
        }
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
            
            roundNum++;
        }
    }
}
