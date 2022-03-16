class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        vector<int> stack;
        int idx = 0;
        int length = pushed.size();
        for (int i = 0; i < length; i++) {
            if (pushed[i] == popped[idx]) {
                idx += 1;
            } else {
                stack.push_back(pushed[i]);
            }
            
            while (idx < length && stack.size() && stack.back() == popped[idx]) {
                stack.pop_back();
                idx += 1;
            }
        }
        return idx == length;
    }
};