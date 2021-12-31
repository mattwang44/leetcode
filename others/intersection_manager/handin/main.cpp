#include <iostream>  
#include <string> 
#include <algorithm>
#include <limits> 
#include <vector>  
#include <cmath>
#include <bitset>
#include <time.h>

#include <iomanip>
using namespace std;

struct Car
{
    unsigned short dir;
    int arr;
    Car(unsigned short d, int r) : dir(d), arr(r) {}
    //bool operator > (const CoordKey& str) const
    //{return (key > str.key);}
};

//Convert binary number to indices of boxes of intersection used
string asBoxIndex(unsigned short dir){
    string str ="";
    if ((!((1&dir)|(2&dir)|(4&dir)|(8&dir))) || dir == 31){str = "0000";}
    else{
        if (1&dir) str += to_string(1&dir);
        if (2&dir) str += to_string(2&dir);
        if (4&dir) str += to_string((4&dir)/4*3);
        if (8&dir) str += to_string((8&dir)/2);
    } return str;
}


int str2bin( char from, char to ){
    if(to != '0'){
        switch (from){
            case 'N':
                switch(to){case 'W': return 2; \
                case 'S': return 6; case 'E': return 14;}
            case 'E':
                switch(to){case 'N': return 1; \
                case 'W': return 3; case 'S': return 7;}
            case 'S':
                switch(to){case 'E': return 8; \
                case 'N': return 9; case 'W': return 11;}
            case 'W':
                switch(to){case 'S': return 4; \
                case 'E': return 12; case 'N': return 13;}
        }
    }
}

string bin2str(unsigned short x){
    switch(x){
        case 31:
            return "00 ";
        case 1:  case 9: case 13:
            return "1N ";
        case 14: case 8: case 12:
            return "1E ";
        case 6:  case 7: case 4:
            return "1S ";
        case 2:  case 3: case 11:
            return "1W ";   
    }
}

// get how many "1" in a binary number (1101 has 3 "1"s)
float CountOne(unsigned short x){
    switch (x){
        case 0:
            return 0;
        case 1: case 2:  case 4:  case 8:
            return 1;
        case 3: case 5:  case 9:  case 6:  case 10:  case 12:
            return 2;
        case 7: case 11: case 13: case 14:
            return 3;       
        case 15:
            return 4; 
        default:
            return -1;
    }
}

// find the multiple Cars that can depart simultaneously
vector<vector<int>> findGroup(vector<unsigned short> vec){
    // 4 cars passing
    if ( (vec[0]+vec[1]+vec[2]+vec[3])==15){return vector<vector<int>>(1,vector<int>{0,1,2,3}); }
    vector<vector<int>> choice; 
    // 3 cars passing (4 boxes used)
    for (int i = 0; i<4; i++){
        int a = i%4, b = (i+1)%4, c = (i+2)%4, d = (i+3)%4;
        if ((CountOne(vec[a]^vec[b]^vec[c])==4)&&((vec[a]|vec[b]|vec[c])==15))
            { choice.push_back( vector<int>(vector<int>{a,b,c}));}
    }//if (choice.size()!=0){return choice;}
    // 3 cars passing (3 boxes used)
    for (int i = 0; i<4; i++){
        int a = i%4, b = (i+1)%4, c = (i+2)%4, d = (i+3)%4;
        if ((CountOne(vec[a]^vec[b]^vec[c])==3)&&(CountOne(vec[a]|vec[b]|vec[c])==3))
            { choice.push_back( vector<int>(vector<int>{a,b,c}));}
    }//if (choice.size()!=0){return choice;}
    // 2 cars passing (4,3,2 boxes used) 
    for (int target = 4; target>=2; target--){
        for (int i = 0; i<4; i++){
            int a = i%4, b = (i+1)%4, c = (i+2)%4, d = (i+3)%4;
            if (((vec[a]&vec[b])==0)&&(CountOne(vec[a]|vec[b])==target)){ choice.push_back( vector<int>{a,b} );}
        }
        if (((vec[0]&vec[2])==0)&&(CountOne((vec[0]|vec[2]))==target)){ choice.push_back( vector<int>{0,2} );}
        if (((vec[1]&vec[3])==0)&&(CountOne((vec[1]|vec[3]))==target)){ choice.push_back( vector<int>{1,3} );}
        if (choice.size()!=0){return choice;}
    }    return choice;
}


vector<int> FindBestGroup(vector<Car> Cars, vector<float> rate){
    vector<unsigned short>list = {Cars[0].dir, Cars[1].dir, Cars[2].dir, Cars[3].dir };
    vector<int>pos =             {Cars[0].arr, Cars[1].arr, Cars[2].arr, Cars[3].arr };
    vector<vector<int>> choices = findGroup(list);
    // single choice
    if (choices.size() == 1){return choices[0];}
    // no pair: find the element with highest rating
    int maxIndex = -1; float max = 0; int minPos=numeric_limits<int>::max();
    if (choices.size() == 0){
        for (int i=0; i<4; i++){if (pos[i]<minPos){minPos = pos[i];}}
        for (int i=0; i<4; i++){if (rate[i] >= max && list[i] != 31 && pos[i]==minPos){ max = rate[i]; maxIndex = i;} }
        return vector<int>(1,maxIndex);
    }
    // multiple choices: find the choice with highest summed rating
    for (int i=0; i<choices.size(); i++){
        float score = 0;
        for (auto emt:choices[i]){score+=rate[emt];}
        if (max<score){maxIndex=i;}
    }return choices[maxIndex];
}
    

float MatchPt(unsigned short x){
    switch (x){/**
        case 0:
            return 0;
        case 1: case 2:  case 4:  case 8:
            return 1;**/
        case 3: case 5:  case 9:  case 6:  case 10:  case 12:
            return 0.3;
        case 7: case 11: case 13: case 14:
            return 2;       
        case 15:
            return 4; 
    }
}

float RateOneCar(vector<vector<Car>> schedule, unsigned short Dir, int atRnd, int scanFrom, int scanTo, float distPt, int len){
    if (Dir == 0 || Dir == 31){return 0;}
    float score = 0; float wd = 0.2, wm = 1;
    for (int a = atRnd + scanTo; a >= atRnd - scanFrom; a--){  
        for (int b = 0; b < 4; b++){
            if (a<0 || a>=len){break;}
            if ( schedule[a][b].dir==31 ){continue;}
            if ( (schedule[a][b].dir!=0) && ((schedule[a][b].dir&Dir)==0) ){
                //distance point: distPt - abs(a-j)
                //matching point: MatchPt(schedule[a][b].dir|Dir)
                score += wd*(distPt - abs(a-atRnd)) + wm*MatchPt(schedule[a][b].dir|Dir);            
            }
        }
    }
    
    return score;
}

vector<vector<float>> Rating(vector<vector<Car>> schedule, int len, int scanFrom, int scanTo, float distRate){
    vector<vector<float>> rate(len+scanTo, vector<float>(4,0));
    int distPt = max(scanFrom, scanTo);
    for (int i = len-1; i >= 0; i--){
        for (int j = 0; j < 4; j++){
            rate[i][j] = RateOneCar(schedule, schedule[i][j].dir, i, scanFrom, scanTo, distPt, len) \
                         + distRate*rate[i+1][j];         
        }
    }
    return rate;
}

int main(int argc, char * argv[]){
    clock_t tStart = clock();
    char str[3], from[3]; int len = numeric_limits<int>::max();
    // open input file
    FILE* file;    file = fopen(argv[1], "r");
    // calculate the length of input
    for(int i = 0; i < len; i++){
        fscanf(file, "%s ", str);
        if (str[0]=='E'){len=i-1;break;}
    }rewind(file);
    // convert the direction of each car to binary and save in a 2D array
    vector<vector<Car>> schedule(len, vector<Car>(4, Car(31,0)));
    for(int i =0;i<4;i++){
        fscanf(file, "%s", from);
        for(int j = 0; j < len; j++){
            fscanf(file, " %s", str);   
            if (str[1]!='0') {schedule[j][i] = Car(str2bin(from[0], str[1]), j);}
            else{schedule[j][i].arr = j;}
        }
    }
    // show the schedule
    // ShowFour(schedule);  ShowBin(schedule); //  Show(schedule);
    schedule.push_back(vector<Car>(4, Car(31,len)));

    

    vector<int> FromArr{2,3,4,6,8,10};  vector<int> ToArr{1,2,3};  vector<float> DistRateArr{0.1,0.25,0.4,0.5,0.75};
    int minRnd = numeric_limits<int>::max();
    for (auto From:FromArr){for (auto To:ToArr){for (auto DistRate:DistRateArr){
        //rate each car by the how important to let the car ge first
        vector<vector<float>> rate = Rating(schedule, len, From, To, DistRate);


        vector<vector<Car>> result;     int head[] = {0,0,0,0};
        
        int round = 0;
        while( head[0]+head[1]+head[2]+head[3] < 4*len ){round += 1;
            for( int i = 0; i < 4; i++){
                while(schedule[head[i]][i].dir==31 && schedule[head[i]][i].arr<round-1 && head[i]<len)
                    {head[i]+=1;}
            }
            if (head[0]+head[1]+head[2]+head[3] >= 4*len){break;}
            vector<int> list = \
            FindBestGroup(vector<Car>{schedule[head[0]][0], schedule[head[1]][1], \
                                      schedule[head[2]][2], schedule[head[3]][3]},\
                          vector<float>{rate[head[0]][0], rate[head[1]][1], rate[head[2]][2], rate[head[3]][3]});

            vector<Car> depart(4, Car(31, 0));
            for (auto ind:list){
                depart[ind] = schedule[head[ind]][ind]; head[ind]+=1;
            }   result.push_back(depart);       
        }
        if (round < minRnd){
            minRnd = round;
            // open output file
            fclose(file); file = fopen(argv[2], "w"); 
            string header[]={"N: ", "E: ", "S: ", "W: "}; int resSize = result.size();
            for (int i=0; i<4; i++){
                fprintf(file, "%s", header[i].c_str());
                for(auto vec:result){fprintf(file,"%s", bin2str(vec[i].dir).c_str());}fprintf(file,"\n");
            }
        }
    }}}
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);tStart = clock();
    return 0;
}
