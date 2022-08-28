import java.io.*;

public class RpsLogicOptimized {
    static int roundNum = 0;
    static char[] myHistory = new char[100000], botHistory = new char[100000];
    
    static char playMove() {
        char move;
        if (roundNum >= 2 && myHistory[roundNum - 1] == myHistory[roundNum - 2]) {
            switch (myHistory[roundNum - 1]) {
                case 'R':
                    move = 'S';
                    break;
                case 'P':
                    move = 'R';
                    break;
                default:
                    move = 'P';
            }
        } else if (roundNum >= 2 && botHistory[roundNum - 1] == botHistory[roundNum - 2]) {
            move = botHistory[roundNum - 1];
        } else {
            // The first move is random, so it doesn't matter what we play
            if (roundNum == 0) {
                move = 'R';
            } else {
                move = myHistory[roundNum - 1];
            }
        }
        
        myHistory[roundNum] = move;
        return move;
    }
    
    static void readBotMove(char botMove) {
        botHistory[roundNum] = botMove;
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
