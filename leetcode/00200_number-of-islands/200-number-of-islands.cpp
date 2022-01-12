class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int R = grid.size();
        int C = grid[0].size();
        int count = 0;
        vector<pair<int, int>> offsets = vector<pair<int, int>>{
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1},
        };
        
        queue<pair<int, int>> q;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == '0') {
                    continue;
                }
                count += 1;
                q.push(pair<int, int>{r, c});
                while (!q.empty()) {
                    pair<int, int> curr = q.front(); q.pop();
                    if (
                        !(0 <= curr.first && curr.first < R) ||
                        !(0 <= curr.second && curr.second < C) ||
                        grid[curr.first][curr.second] == '0'
                    ) {
                        continue;
                    }
                    grid[curr.first][curr.second] = '0';
                    for (auto offset : offsets) {
                        q.push({
                            curr.first + offset.first,
                            curr.second + offset.second,
                        });
                    }
                    
                }
            }
        }
        return count;
    }
};
