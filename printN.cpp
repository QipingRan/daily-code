#include <iostream>
using namespace std;

void PrintN(int N)
{
    if(N){
        PrintN(N-1);
        printf("%d\n",N);
    }
    return;


}
int main()
{
//    int i;
//    for(i=1;i<=1000;i++){
//        printf("%d\n",i);
//    }
    PrintN(1000);

    return 0;
}

//1.509s's =using time
