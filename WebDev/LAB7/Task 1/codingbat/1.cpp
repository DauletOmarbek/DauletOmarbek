#include <iostream>
#include <math.h>
using namespace std;
double factorial(int f){
    if(f==1){
    return 1;
    }
    else
    {
        f=f*factorial(f-1);
        return f;
    }
}
int main(){
    setlocale(LC_ALL,"Russian");
    float summa;
    int n; //dlina ryada
    cout<<"Введите длину ряда: ";
    cin>>n;
summa=0;
for(int i=1;i<=n;i++){
    summa=summa+1/factorial(i);
}
cout<<"Сумма: "<<summa<<endl;
}