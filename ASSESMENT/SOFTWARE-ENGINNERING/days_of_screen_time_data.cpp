#include<iostream>
using namespace std;
int main(){
    int screentime[7] ,i ,sum=0;

    cout<<"enter your screen time";
    for(i=0;i<7;i++){
    cin>>screentime[i];
    sum += screentime[i];
    }

    cout<<"total sum = "<<sum<<"\n";
    float avg = sum / 7.0;
    cout<<"avarage"<<avg;

    cout<<"\n";
    if(avg > 10){
     cout<<"  Warning: Too much screen time!";
    }
}
