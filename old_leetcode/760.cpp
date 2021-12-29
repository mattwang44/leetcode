// 1st try: Jan. 17, 2018
// https://leetcode.com/problems/find-anagram-mappings/description/
// time: O(n^2)
// space: O(n)
class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        int dgt = A.size(); int bias = 0; int count = 0; 
        vector<int> result(dgt, -1);
        for (int k = 0; k < dgt; k++){
            for (int i = 0; i < dgt; i++){
                if (A[i] == B[i]) {
                    result[i] = i+bias <= dgt-1 ? i+bias : i+bias-dgt;
                    A[i] = -1; count++;
                }
            }
            if (count == dgt){break;}
            bias++; 
            B.push_back(B[0]); B.erase(B.begin());
        }
        return result;
    }    
};

// solution form forum: Hash Table