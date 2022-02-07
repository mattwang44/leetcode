class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        // constants
        int EMPTY = pow(2, 31) - 1;
        int WALL = -1;
        int GATE = 0;

        int R = rooms.size(), C = rooms[0].size();
        queue<vector<int>> q;

        // gather gates
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (rooms[r][c] == GATE) {
                    q.push(vector<int>{r, c, 0});
                }
            }
        }

        vector<pair<int, int>> offsets = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1},
        };

        // bfs
        while (!q.empty()) {
            vector<int> node = q.front(); q.pop();
            int r = node[0];
            int c = node[1];
            int step = node[2];

            for (auto offset: offsets) {
                int _r = r + offset.first;
                int _c = c + offset.second;

                if (_r < 0 || _r >= R || _c < 0 || _c >= C || rooms[_r][_c] != EMPTY) {
                    continue;
                }

                rooms[_r][_c] = step + 1;
                q.push({_r, _c, step + 1});
            }            
        }
    }
};
