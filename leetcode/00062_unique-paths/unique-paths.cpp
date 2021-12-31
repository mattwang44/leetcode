class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 1 || n == 1) {
            return 1;
        }

        vector<int> memo(n - 1, 0);
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                memo[j] = i == 0 ? 1 : memo[j];
                memo[j] += j == 0 ? 1 : memo[j - 1];
            }
        }
        return memo[n - 2];
    }
};