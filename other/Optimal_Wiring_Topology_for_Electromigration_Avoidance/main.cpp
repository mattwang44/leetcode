#include <iostream>  
#include <string> 
#include <algorithm>
#include <limits> 
#include <vector>  
#include <cmath>
#include <time.h>
using namespace std;

struct CoordKey
{
    int key, s, t;
    CoordKey(int k, int x, int y) : key(k), s(x), t(y) {}
    bool operator > (const CoordKey& str) const
    {return (key > str.key);}
};

void heapify(vector<CoordKey> &vec, int n, int i)
{
    int largest = i;  // Initialize largest as root
    int l = 2*i + 1;  // left = 2*i + 1
    int r = 2*i + 2;  // right = 2*i + 2
 
    if (l < n && vec[l] > vec[largest])        largest = l;
    if (r < n && vec[r] > vec[largest])        largest = r;
    if (largest != i)
    {
        CoordKey a1 = vec[i];   vec[i] = vec[largest];  vec[largest] = a1;
        heapify(vec, n, largest);
    }
}
 
void heapSort(vector<CoordKey> &vec, int n)
{
    for (int i = n/2 ; i >= 0; i--)
        heapify(vec, n, i);
    for (int i=n-1; i>=0; i--)
    {
        CoordKey a = vec[0];        vec[0] = vec[i];        vec[i] = a;
        heapify(vec, i, 0);
    }
}


int main(int argc, char * argv[]){
    clock_t tStart = clock();/////////
    
    FILE* file; int count, xc, yc, flow;
    file = fopen(argv[1], "r");
    fscanf(file, "%d\t\t", &count);		// 1st line: total number of point
    vector<vector<int>> source, sink;
    for(int i=0; i<count; i++){			// other lines: x-coord, y-coord, value
        fscanf(file, "%d\t%d\t%d", &xc, &yc, &flow);
        vector<int> vec{xc, yc, flow};
        if (flow > 0){ source.push_back(vec); }
        else         { sink.push_back(vec); }
    }
    

    int m = source.size(); int n = sink.size(); int area = 0;


     
    fclose(file); file = fopen(argv[2], "w"); 
    vector<CoordKey> cost; int dist;
    vector<vector<vector<int>>> record(m, vector<vector<int>>(n,vector<int>(5,0))); // 0distance, 1flow(also cap. of neg flow), 2+capacity
    for (int i = 0; i<m; i++){	
        for (int j = 0; j<n; j++){	
            //(abs(source[i][0]-sink[j][0]) + abs(source[i][1]-sink[j][1])) * min(source[i][2], -sink[j][2])
            dist = (abs(source[i][0]-sink[j][0]) + abs(source[i][1]-sink[j][1]));
            CoordKey c(dist , i, j);
            cost.push_back(c); record[i][j][0] = dist;  record[i][j][2] = min(source[i][2], -sink[j][2]);
        }
    }


    heapSort(cost, m*n);


    int row, col;
    for (int i = 0; i < m*n; i++){
        row = cost[i].s; col = cost[i].t;  
        if (source[row][2] == 0 || sink[col][2] == 0) {continue;}
        if (source[row][2] >= -sink[col][2]){
             
            record[row][col][1] -= sink[col][2]; record[row][col][2] += sink[col][2]; 
            source[row][2] = source[row][2] + sink[col][2]; sink[col][2] = 0;
            
       }
       
       else{
            record[row][col][1] += source[row][2]; record[row][col][2] -= source[row][2]; 
            sink[col][2] = sink[col][2] + source[row][2]; source[row][2] = 0;
       }
    }




    bool bk; vector<int> cycle; int temp; int temp_end; int remd; int a, b; int size;

    bool negCycle = true;
    while(negCycle){
    vector<int> sp(n, numeric_limits<int>::max());  //shortest path
    auto it = sp.begin(); sp.insert(it, m, 0);
    vector<int> pred(n+m, -1);                      //pred.
        negCycle = false; bk = false;
        for (int k=0;k<m+n;k++){
            for (int i=0;i<m;i++){for(int j=0;j<n;j++){
                if (record[i][j][2] == 0){continue;}
                if (sp[m+j] > sp[i] + record[i][j][0])
                    {sp[m+j] = sp[i] + record[i][j][0]; pred[m+j] = i;}
            }}

            for (int i=0;i<m;i++){for(int j=0;j<n;j++){
                if (record[i][j][1] == 0){continue;}
                if (sp[i] > sp[m+j] - record[i][j][0])
                    {sp[i] = sp[m+j] - record[i][j][0]; pred[i] = j+m;}
            }}

        }

        //last cycle
        for (int i=0;i<m;i++){if (bk){break;} for(int j=0;j<n;j++){
            if (record[i][j][2] == 0){continue;}
            if (sp[m+j] > sp[i] + record[i][j][0])
                {negCycle = true;bk = true; break;}
        }}

        for (int i=0;i<m;i++){ if (bk){break;} for(int j=0;j<n;j++){
            if (record[i][j][1] == 0){continue;}
            if (sp[i] > sp[m+j] - record[i][j][0])
                {negCycle = true;bk = true; break;}
        }}


        if(negCycle == true){
            temp = 0;cycle.clear();remd = numeric_limits<int>::max();
            while(true){
                if(std::find(cycle.begin(), cycle.end(), temp) != cycle.end()) { 
                     cycle.clear();  break;
                }
                else{cycle.push_back(temp); temp_end = temp; temp = pred[temp];}
            }
            while(true){
                cycle.push_back(temp); temp = pred[temp]; if (temp == temp_end){ cycle.push_back(temp); break;}
                
            }

            size = cycle.size();           
            for (int i=0;i<size;i++){
                if (i == size-1){a = cycle[i]; b = cycle[0];}
                else          {a = cycle[i]; b = cycle[i+1];}

                if (a < b){  
                    if (record[a][b - m][1]<remd) {remd = record[a][b - m][1];} }
                else {
                    if (record[b][a - m][2]<remd) {remd = record[b][a - m][2];} }
            }

            
            for (int i=0;i<size;i++){
                if (i == size-1){a = cycle[i]; b = cycle[0];}
                else          {a = cycle[i]; b = cycle[i+1];}

                if (a < b){  
                    record[a][b - m][1] -= remd;  record[a][b - m][2] += remd;
                }
                else{   
                    record[b][a - m][2] -= remd;  record[b][a - m][1] += remd;
                }
            }
     
        }
    }

    for (int i=0;i<m;i++){for(int j=0;j<n;j++){
        if (record[i][j][1] == 0){continue;}
        area += record[i][j][0] * record[i][j][1];
    }} fprintf(file, "%d\n", area);
    for (int i=0;i<m;i++){for(int j=0;j<n;j++){
        if (record[i][j][1] == 0){continue;}
        fprintf(file, "%d\t%d\t%d\t%d\t%d\n", source[i][0], source[i][1], sink[j][0], sink[j][1], record[i][j][1]);
    }}

    
    fclose(file);
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);tStart = clock();/////////////////////

    
    return 0;
}
