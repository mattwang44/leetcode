// 1st try: Jan. 17, 2018
// https://leetcode.com/problems/complex-number-multiplication/description/

class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        char ar[4], br[4], ai[4], bi[4];  
        bool st = true; int pos;
        for (int i = 0; i < a.size(); i++){
            if (a[i] == '+'){st = false; pos = i+1; continue;}
            if (st) {ar[i] = a[i]; } 
            else    {ai[i-pos]= a[i]; }
        }   st = true; ar[pos-1] = '\0';
        for (int i = 0; i < b.size(); i++){
            if (b[i] == '+'){st = false; pos = i+1; continue;}
            if (st) {br[i] = b[i]; } 
            else    {bi[i-pos]= b[i]; }
        } br[pos-1] = '\0';
        cout<<atoi(ar)<<","<<atoi(br)<<", "<<atoi(ai)<<","<<atoi(bi);
        return to_string(atoi(ar)*atoi(br)-atoi(ai)*atoi(bi)) + "+" +\
            to_string(atoi(ar)*atoi(bi)+atoi(br)*atoi(ai))+"i";
    }
    
};