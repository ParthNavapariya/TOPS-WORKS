#include<iostream>
#include<fstream>
using namespace std;

int main(){
    int choice;
    string goal;

    cout << "1. Write Goals\n2. Read Goals\nEnter choice: ";
    cin >> choice;

    if(choice == 1){
        ofstream file("goals.txt", ios::app); // write mode

        cout << "Enter your goal: ";
        cin.ignore();
        getline(cin, goal);

        file << goal << endl;
        file.close();

        cout << "Goal saved successfully!";
    }
    else if(choice == 2){
        ifstream file("goals.txt"); // read mode

        cout << "Your goals are:\n";
        while(getline(file, goal)){
            cout << goal << endl;
        }

        file.close();
    }
    else{
        cout << "Invalid choice!";
    }

    return 0;
}