#include <iostream>
using namespace std;
int main(){
int N;
cin >> N;
int tmp;
int mass[N];
for (int i = 0; i < N; i++)
{
    cin >> mass[i];
}



    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N-1; j++)
        {
            if (mass[i] < 0 && mass[i] < mass[j]) {

                    tmp = mass[i];
                    mass[i] = mass[j];
                    mass[j] = tmp;


            }
            else
            {
                if (mass[i] > 0) {
                    if (mass[i] < mass[j])
                {
                    tmp = mass[i];
                    mass[i] = mass[j];
                    mass[j] = tmp;

                }
                }
            }

        }
    }
    for (int i = N-1; i >= 0; i--)
    {
        cout << mass[i] << " ";
    }
    
}