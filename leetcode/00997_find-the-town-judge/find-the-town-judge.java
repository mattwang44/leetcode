class Solution {
    public int findJudge(int n, int[][] trust) {
        if (trust.length < n - 1) {
            return -1;
        }
        int[] candidates = new int[n];
        int[] impossible = new int[n];
        for (int[] relation : trust) {
            candidates[relation[1] - 1]++;
            impossible[relation[0] - 1]++;
        }
        for (int i = 0; i < n; i++) {
            if (candidates[i] == n - 1 && impossible[i] == 0) {
                return i + 1;
            }
        }
        return -1;
    }
}