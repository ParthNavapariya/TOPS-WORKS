// 1. Conditional Logic Implementation
// Design a “Study Mood Assistant” that:
// ● Takes user input: hours studied today
// ● Displays motivation messages based on conditions
// ● Uses if-else ladder or switch case


#include<iostream>
using namespace std;
int main(){
    int hour;
    cout<<"enter your studiess houre";
    cin>>hour;

    if(hour < 1){
        cout<<"You haven’t started yet! Begin with just 1 hour — small steps lead to big success.";
    }
    else if(hour <= 2){
        cout<<"Good start! Keep pushing a little more — you can do better";
    }
    else if(hour <= 4){
        cout<<"Nice work! You’re building consistency — keep it up";
    }
    else if(hour <= 6){
        cout<<"Great effort! You’re serious about your goals — be proud!";
    }
    else if(hour <= 8){
        cout<<"Excellent dedication! You’re on the path to becoming a top performer!";
    }
    else {
        cout<<"Outstanding! You were in beast mode today — success is near!";
    }
}