#include <iostream>
#include <vector>
using namespace std;

struct ColKey
{
    int key, col;
    ColKey(int k, int s) : key(k), col(s) {}
    bool operator > (const ColKey& str) const
    {return (key > str.key);}
};

void heapify(vector<ColKey> &vec, int n, int i)
{
    int largest = i;  // Initialize largest as root
    int l = 2*i + 1;  // left = 2*i + 1
    int r = 2*i + 2;  // right = 2*i + 2
 
    // If left child is larger than root
    if (l < n && vec[l] > vec[largest])        largest = l;
 
    // If right child is larger than largest so far
    if (r < n && vec[r] > vec[largest])        largest = r;
    
    // If largest is not root
    if (largest != i)
    {
        // swap 
        ColKey a1 = vec[i];   vec[i] = vec[largest];  vec[largest] = a1;

        // Recursively heapify the affected sub-tree
        heapify(vec, n, largest);
    }
}
 
// function to do heap sort
void heapSort(vector<ColKey> &vec, int n)
{
    // Build heap (rearrange array as max heap)
    for (int i = n/2 ; i >= 0; i--)
        heapify(vec, n, i);

    cout<<"After buildheap(): \n";
    for (int i=0; i<n; i++) {cout<<vec[i].key<<' ';} cout<<'\n';
    for (int i=0; i<n; i++) {cout<<vec[i].col<<' ';} cout<<'\n'<<'\n';
 
    // One by one extract an element from heap
    for (int i=n-1; i>=0; i--)
    {
        // Move current root to end
        ColKey a = vec[0];        vec[0] = vec[i];        vec[i] = a;

        // call max heapify on the reduced heap
        heapify(vec, i, 0);
    }
}

int main()
{
    // s(i)
    int arr_s[] = {1,3,0,3,6,5};
    int n_s = sizeof(arr_s)/sizeof(arr_s[0]);

    // f(i)
    int arr_f[] = {6,9,4,10,11,7};
    int n_f = sizeof(arr_f)/sizeof(arr_f[0]);

    // vectoriztion: merge s(i) and f(i)
    int n = n_s + n_f;
    vector<ColKey> vec;
    for (int i=0; i<n_s; i++) {vec.push_back(ColKey(arr_s[i], 1));}
    for (int i=0; i<n_f; i++) {vec.push_back(ColKey(arr_f[i], -1));}
    cout << "Initial data: \n"<<"s(i) = [ ";
    for (int i=0; i<n_s; i++) {cout<<vec[i].key<<' ';} cout<<"]\n"<<"f(i) = [ ";
    for (int i=n_s; i<n; i++) {cout<<vec[i].key<<' ';} cout<<"]\n"<<'\n';

    // heap sort
    heapSort(vec, n);
    cout << "After sorting: \n";
    for (int i=0; i<n; i++) {cout<<vec[i].key<<' ';} cout<<'\n';
    for (int i=0; i<n; i++) {cout<<vec[i].col<<' ';} cout<<'\n'<<'\n';
    
    int sum = 0, l = 0;
    for (int i=0; i<n; i++) 
    {
        sum += vec[i].col;
        if ((vec[i].key != vec[i+1].key) && (sum > l)) {l = sum;}
    } cout<<"The depth is "<<l<<'\n';
}