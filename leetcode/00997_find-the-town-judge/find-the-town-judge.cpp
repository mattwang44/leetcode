class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        map<int, int> candidates;
        map<int, int> impossible;
        for (auto relation : trust) {
            candidates[relation[1]] += 1;
            impossible[relation[0]] += 1;
        }
        for (int i = 1; i <= n; i++) {
            if (candidates[i] == n - 1 && impossible[i] == 0) {
                return i;
            }
        }
        return -1;
    }
};