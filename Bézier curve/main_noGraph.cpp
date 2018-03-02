#include <iostream>  
#include <string>  
#include <fstream>  
#include <vector>  
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include "gnuplot_i.hpp"
#include <time.h>

using namespace std;

// Class of a point
class Point{
public:
    double x;                 // X coord.
    double y;                 // Y coord.
    Point(double, double);    // Constructor with assigned X and Y
};
Point::Point(double a, double b){x=a;y=b;}

// Lerp of two points
Point Lerp(Point a, Point b, double t){
    Point ans((1 - t) * a.x + t * b.x, (1 - t) * a.y + t * b.y);
    return ans;
}

// Berzier Curve
Point Bezier(vector<vector<Point>> mat, double t){
    // Number of input points
    int N_in = mat.size();

    // Recursive function
    for (int i=1; i<N_in; i++){
        for (int j=i; j<N_in; j++){
            mat[i][j] = Lerp(mat[i-1][j-1], mat[i-1][j], t); } }

    // Return the point of (N_in - 1) degree Berzier Curve
    return mat[N_in-1][N_in-1];
}

int main(int argc, char * argv[]){
    clock_t tStart = clock();
    // Open input file (1st argument)
    char line[100];
    ifstream file_in;
    file_in.open(argv[1]);

    // Open output file (2nd argument)
    ofstream file_out;
    file_out.open(argv[2]);
    
    // Parsing the number of input points, N_in
    file_in.getline(line,sizeof(line),'\n');
    int N_in = atoi(line);

    // Parsing the coordinates of the control points
    Point Init(0,0);
    vector<Point> CtrlPt(N_in, Init); //vector of control points
    string str; int found;
    for (int i=0; i<N_in; i++){
        file_in.getline(line,sizeof(line),'\n');
        str = line;  found = str.find(" ");        
        CtrlPt[i].x = stof(str.substr(0,found));
        CtrlPt[i].y = stof(str.substr(found,str.size()));
    }

    // Parsing the number of sampling points, N_sp
    file_in.getline(line,sizeof(line),'\n');
    int N_sp = atoi(line);
    file_in.close(); 
    
    // Initialization of the matrix for recording the value
    vector<vector<Point>> mat_init(N_in, vector<Point>(N_in, Init));
    // The points in the first row are the control points
    for (int i = 0; i < N_in; i++){mat_init[0][i] = CtrlPt[i];}
   
    // Invoke the function with different value of t
    double t = 1/(double(N_sp)-1);  Point ANS(0,0);
    for (int i = 0; i < N_sp; i++){
        ANS = Bezier(mat_init, t*i);
        file_out << fixed  <<  setprecision(2) << ANS.x << "\t" << ANS.y <<"\n"; // for output file
    }
    file_out.close(); 

    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
