import java.io.*;
import java.util.List;
import java.util.ArrayList;

public class HaikuPartition {
    // You can programatically generate these line structures too! See the Python solution
    static int[][] FIVES = {
        {5}, {4, 1}, {3, 2}, {3, 1, 1}, {2, 2, 1}, {2, 1, 1, 1}, {1, 1, 1, 1, 1}
    };
    static int[][] SEVENS = {
        {7}, {6, 1}, {5, 2}, {5, 1, 1}, {4, 3}, {4, 2, 1}, {4, 1, 1, 1},
        {3, 3, 1}, {3, 2, 2}, {3, 2, 1, 1}, {3, 1, 1, 1, 1}, {2, 2, 2, 1},
        {2, 2, 1, 1, 1}, {2, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1}
    };
    
    static void solve(int N, int[] S, String[] W) {
        List<List<String>> wordBank = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            wordBank.add(new ArrayList<>());
        }
        for (int i = 0; i < N; i++) {
            int syllables = S[i];
            String word = W[i];
            wordBank.get(syllables).add(word);
        }
        
        int[][] structure = findValidStructure(wordBank);
        if (structure != null) {
            for (int[] line : structure) {
                List<String> lineWords = new ArrayList<>();
                for (int syllables : line) {
                    List<String> words = wordBank.get(syllables);
                    lineWords.add(words.remove(words.size() - 1));
                }
                System.out.println(String.join(" ", lineWords));
            }
        } else {
            System.out.println("IMPOSSIBLE\nIMPOSSIBLE\nIMPOSSIBLE");
        }
    }
    
    static int[][] findValidStructure(List<List<String>> wordBank) {
        for (int[] line1 : FIVES) {
            for (int[] line2 : SEVENS) {
                for (int[] line3 : FIVES) {
                    if (isStructureValid(wordBank, line1, line2, line3)) {
                        return new int[][] {line1, line2, line3};
                    }
                }
            }
        }
        return null;
    }
    
    static boolean isStructureValid(List<List<String>> wordBank, int[] line1, int[] line2, int[] line3) {
        int[] syllableCount = new int[10];
        for (int syllable : line1) {
            syllableCount[syllable] += 1;
        }
        for (int syllable : line2) {
            syllableCount[syllable] += 1;
        }
        for (int syllable : line3) {
            syllableCount[syllable] += 1;
        }
        
        for (int syllables = 1; syllables < 10; syllables++) {
            if (wordBank.get(syllables).size() < syllableCount[syllables]) {
                return false;
            }
        }
        return true;
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
