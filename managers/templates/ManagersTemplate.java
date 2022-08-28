import java.io.*;

public class ManagersTemplate {
    /**
     * Find the most possible disputes a single employee is responsible for 
     * resolving at the company.
     * 
     * N: the number of employees in the company
     * M: the list of integers denoting the employee number of each individual's manager
     */
    static long solve(int N, int[] M) {
        // YOUR CODE HERE
        return 0;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            String info[] = in.readLine().split(" ");
            int[] M = new int[info.length];
            for (int j = 0; j < info.length; j++) {
                M[j] = Integer.parseInt(info[j]);
            }
            System.out.println(solve(N, M));
        }
        out.flush();
    }
}
