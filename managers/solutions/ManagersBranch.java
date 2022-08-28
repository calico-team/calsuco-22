import java.io.*;

import java.util.List;
import java.util.ArrayList;

public class ManagersBranch {
    static long solve(int N, int[] M) {
        List<List<Integer>> subordinates = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            subordinates.add(new ArrayList<>());
        }
        for (int i = 1; i < N; i++) {
            subordinates.get(M[i]).add(i);
        }
        
        int branchSizes[] = new int[N];
        findBranchSizeDFS(0, subordinates, branchSizes);

        // Since there can be up to 10 ** 5 employees, there can be up to ~10 ** 10
        // unique disputes. To represent the worst case where all of them are resolved
        // by the CEO, we need to use 64 bits instead.
        long mostDisputes = 0;
        for (int i = 0; i < N; i++) {
            mostDisputes = Math.max(mostDisputes, disputesResolvedBy(i, subordinates, branchSizes));
        }
        return mostDisputes;
    }

    static int findBranchSizeDFS(int id, List<List<Integer>> subordinates, int[] branchSizes) {
        branchSizes[id] = 1;
        for (int sub : subordinates.get(id)) {
            branchSizes[id] += findBranchSizeDFS(sub, subordinates, branchSizes);
        }
        return branchSizes[id];
    }

    static long disputesResolvedBy(int id, List<List<Integer>> subordinates, int[] branchSizes) {
        if (subordinates.get(id).size() == 0) {
            return 0;
        } else if (subordinates.get(id).size() == 1) {
            long selfDisputes = branchSizes[id] - 1;
            return selfDisputes;
        } else {
            long selfDisputes = branchSizes[id] - 1;

            long leftBranchSize = branchSizes[subordinates.get(id).get(0)];
            long rightBranchSize = branchSizes[subordinates.get(id).get(1)];
            long crossBranchDisputes = leftBranchSize * rightBranchSize;

            return selfDisputes + crossBranchDisputes;
        }
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
