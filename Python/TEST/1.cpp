#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
int a;
cin >> a;
vector <int> v;
for (int i = 0; i < a; i++)
{
    int b;
    cin >> b;
    v.push_back(b);
}
sort(v.begin(),v.end());
reverse(v.begin(),v.end());

for (int i = 0; i < a; i++)
{
    cout << v[i] << " ";
}





}